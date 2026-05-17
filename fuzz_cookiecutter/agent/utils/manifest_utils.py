from __future__ import annotations

import base64
import json
import os
from collections import OrderedDict
from pathlib import Path
from typing import Any

from cookiecutter.generate import generate_context
from cookiecutter.prompt import prompt_for_config
from cookiecutter.utils import create_env_with_context
from fuzz_cookiecutter.agent.models import InvocationConfig, ManifestExecutionSpec
from fuzz_cookiecutter.agent.utils.monitoring import trace

SUPPORTED_OUTPUT_DIR_STATES = {"missing", "existing_empty", "project_exists"}
SUPPORTED_HOOKS = {"pre_prompt", "pre_gen_project", "post_gen_project"}


class ManifestValidationError(ValueError):
    """Raised when a generated manifest is invalid."""


def _require_keys(payload: dict[str, Any], keys: set[str], label: str) -> None:
    missing = keys - set(payload)
    if missing:
        msg = f"{label} missing keys: {sorted(missing)}"
        raise ManifestValidationError(msg)


def _assert_relative_path(raw_path: str, *, label: str) -> None:
    path = Path(raw_path)
    if path.is_absolute():
        raise ManifestValidationError(f"{label} must be relative: {raw_path}")
    if ".." in path.parts:
        raise ManifestValidationError(f"{label} must not escape via '..': {raw_path}")


def _decode_binary(contents: str) -> bytes:
    try:
        return base64.b64decode(contents, validate=True)
    except Exception as exc:
        raise ManifestValidationError("Binary contents are not valid base64") from exc


def _write_file(path: Path, contents: bytes | str, *, binary: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if binary:
        path.write_bytes(contents if isinstance(contents, bytes) else contents.encode("utf-8"))
    else:
        path.write_text(contents if isinstance(contents, str) else contents.decode("utf-8"), encoding="utf-8")


def _build_cookiecutter_context(template_config_path: Path) -> dict[str, Any]:
    trace("manifest", "building projected cookiecutter context", template_config_path=template_config_path)
    context = generate_context(str(template_config_path))
    try:
        prompted = prompt_for_config(context, no_input=True)
    except Exception:  # noqa: BLE001
        prompted = {}
        trace("manifest", "prompt projection failed, using empty prompt overrides", template_config_path=template_config_path)
    context["cookiecutter"].update(prompted)
    trace("manifest", "projected cookiecutter context ready", keys=len(context.get("cookiecutter", {})))
    return context


def validate_manifest_payload(payload: dict[str, Any]) -> None:
    trace("manifest", "validating manifest payload")
    _require_keys(payload, {"mode", "template_source", "template", "invocation"}, "manifest")
    if payload["mode"] not in {"cli", "api"}:
        raise ManifestValidationError("mode must be 'cli' or 'api'")
    if payload["template_source"] != "local":
        raise ManifestValidationError("template_source must be 'local' in version 1")

    template = payload["template"]
    if not isinstance(template, dict):
        raise ManifestValidationError("template must be an object")
    _require_keys(
        template,
        {
            "root_name",
            "cookiecutter_json",
            "prompts",
            "copy_without_render",
            "new_lines",
            "files",
            "hooks",
            "nested_templates",
        },
        "template",
    )
    if not isinstance(template["cookiecutter_json"], dict):
        raise ManifestValidationError("template.cookiecutter_json must be an object")
    if not isinstance(template["prompts"], dict):
        raise ManifestValidationError("template.prompts must be an object")
    if not isinstance(template["copy_without_render"], list):
        raise ManifestValidationError("template.copy_without_render must be a list")
    if template["new_lines"] not in ("\n", "\r\n", None):
        raise ManifestValidationError("template.new_lines must be '\\n', '\\r\\n', or null")
    if not isinstance(template["files"], list):
        raise ManifestValidationError("template.files must be a list")
    if not isinstance(template["hooks"], dict):
        raise ManifestValidationError("template.hooks must be an object")
    _require_keys(template["hooks"], SUPPORTED_HOOKS, "template.hooks")

    for file_entry in template["files"]:
        if not isinstance(file_entry, dict):
            raise ManifestValidationError("file entry must be an object")
        _require_keys(file_entry, {"path", "kind", "contents"}, "file entry")
        _assert_relative_path(file_entry["path"], label="file path")
        if file_entry["kind"] not in {"text", "binary"}:
            raise ManifestValidationError("file kind must be 'text' or 'binary'")
        if file_entry["kind"] == "binary":
            _decode_binary(file_entry["contents"])

    for hook_name, hook_body in template["hooks"].items():
        if hook_name not in SUPPORTED_HOOKS:
            raise ManifestValidationError(f"unsupported hook {hook_name}")
        if hook_body is not None and not isinstance(hook_body, str):
            raise ManifestValidationError("hook bodies must be strings or null")

    nested_templates = template["nested_templates"]
    if nested_templates is not None:
        if not isinstance(nested_templates, list) or not nested_templates:
            raise ManifestValidationError("nested_templates must be a non-empty list or null")
        for item in nested_templates:
            _require_keys(item, {"key", "path", "title", "description"}, "nested template")
            _assert_relative_path(item["path"], label="nested template path")

    invocation = payload["invocation"]
    if not isinstance(invocation, dict):
        raise ManifestValidationError("invocation must be an object")
    _require_keys(
        invocation,
        {
            "no_input",
            "extra_context",
            "replay",
            "overwrite_if_exists",
            "skip_if_file_exists",
            "accept_hooks",
            "keep_project_on_failure",
            "output_dir_state",
        },
        "invocation",
    )
    if not isinstance(invocation["no_input"], bool):
        raise ManifestValidationError("invocation.no_input must be a boolean")
    if not isinstance(invocation["extra_context"], dict):
        raise ManifestValidationError("invocation.extra_context must be an object")
    if invocation["replay"] is not None and not isinstance(invocation["replay"], dict):
        raise ManifestValidationError("invocation.replay must be an object or null")
    if invocation["replay"] is not None and invocation["extra_context"]:
        raise ManifestValidationError("replay and extra_context are mutually exclusive")
    if invocation["replay"] is not None and invocation["no_input"]:
        raise ManifestValidationError("replay cannot be combined with no_input=true")
    if invocation["output_dir_state"] not in SUPPORTED_OUTPUT_DIR_STATES:
        raise ManifestValidationError("Unknown output_dir_state value")
    trace("manifest", "manifest payload validation passed", mode=payload["mode"], template_source=payload["template_source"])


def _project_dir_from_context(root_name: str, context: dict[str, Any]) -> str:
    env = create_env_with_context(context)
    try:
        rendered = env.from_string(root_name).render(**context)
    except Exception:  # noqa: BLE001
        return "predicted_project"
    return rendered or "predicted_project"


def _materialize_nested_templates(
    payload: dict[str, Any], template_root: Path
) -> tuple[dict[str, Any], Path]:
    template = payload["template"]
    nested_templates = template["nested_templates"]
    assert nested_templates is not None
    trace("manifest", "materializing nested templates", count=len(nested_templates), template_root=template_root)
    base_context = OrderedDict([("templates", OrderedDict())])
    selected_path = None
    for index, nested in enumerate(nested_templates):
        nested_dir = template_root / nested["path"]
        nested_dir.mkdir(parents=True, exist_ok=True)
        trace("manifest", "created nested template directory", index=index, path=nested_dir)
        nested_cc = OrderedDict(template["cookiecutter_json"])
        if template["prompts"]:
            nested_cc["__prompts__"] = OrderedDict(template["prompts"])
        if template["copy_without_render"]:
            nested_cc["_copy_without_render"] = list(template["copy_without_render"])
        if template["new_lines"] is not None:
            nested_cc["_new_lines"] = template["new_lines"]
        (nested_dir / "cookiecutter.json").write_text(
            json.dumps(nested_cc, indent=2), encoding="utf-8"
        )
        materialize_template_files(template, nested_dir)
        materialize_hooks(template["hooks"], nested_dir)
        base_context["templates"][nested["key"]] = {
            "path": nested["path"],
            "title": nested["title"],
            "description": nested["description"],
        }
        if index == 0:
            selected_path = nested_dir
    if selected_path is None:
        raise ManifestValidationError("No nested template choices were produced")
    trace("manifest", "nested templates materialized", selected_path=selected_path)
    return base_context, selected_path


def materialize_template_files(template: dict[str, Any], template_root: Path) -> None:
    rendered_root = template_root / template["root_name"]
    rendered_root.mkdir(parents=True, exist_ok=True)
    trace("manifest", "materializing template files", rendered_root=rendered_root, file_count=len(template["files"]))
    for file_entry in template["files"]:
        relative_path = Path(file_entry["path"])
        destination = rendered_root / relative_path
        if file_entry["kind"] == "binary":
            _write_file(destination, _decode_binary(file_entry["contents"]), binary=True)
        else:
            _write_file(destination, file_entry["contents"], binary=False)
        trace("manifest", "wrote template file", destination=destination, kind=file_entry["kind"])


def materialize_hooks(hooks: dict[str, Any], template_root: Path) -> None:
    hooks_dir = template_root / "hooks"
    trace("manifest", "materializing hooks", template_root=template_root)
    for hook_name, hook_body in hooks.items():
        if hook_body is None:
            trace("manifest", "skipped empty hook", hook_name=hook_name)
            continue
        hooks_dir.mkdir(parents=True, exist_ok=True)
        hook_path = hooks_dir / f"{hook_name}.py"
        hook_path.write_text(hook_body, encoding="utf-8")
        trace("manifest", "wrote hook file", hook_name=hook_name, hook_path=hook_path)


def materialize_manifest(manifest_path: Path, workspace_dir: Path) -> ManifestExecutionSpec:
    trace("manifest", "loading manifest file", manifest_path=manifest_path, workspace_dir=workspace_dir)
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    validate_manifest_payload(payload)
    workspace_dir.mkdir(parents=True, exist_ok=True)
    trace("manifest", "created workspace directory", workspace_dir=workspace_dir)
    template_repo_dir = workspace_dir / "template_repo"
    template_repo_dir.mkdir(parents=True, exist_ok=True)
    output_dir = workspace_dir / "output"
    trace("manifest", "created template repo directory", template_repo_dir=template_repo_dir)

    template = payload["template"]
    invocation = payload["invocation"]
    selected_template_dir = template_repo_dir
    if template["nested_templates"] is None:
        trace("manifest", "materializing standard template repository")
        cookiecutter_json = OrderedDict(template["cookiecutter_json"])
        if template["prompts"]:
            cookiecutter_json["__prompts__"] = OrderedDict(template["prompts"])
        if template["copy_without_render"]:
            cookiecutter_json["_copy_without_render"] = list(template["copy_without_render"])
        if template["new_lines"] is not None:
            cookiecutter_json["_new_lines"] = template["new_lines"]
        (template_repo_dir / "cookiecutter.json").write_text(
            json.dumps(cookiecutter_json, indent=2), encoding="utf-8"
        )
        materialize_template_files(template, template_repo_dir)
        materialize_hooks(template["hooks"], template_repo_dir)
    else:
        trace("manifest", "materializing template repository with nested templates")
        cookiecutter_json, selected_template_dir = _materialize_nested_templates(
            payload, template_repo_dir
        )
        (template_repo_dir / "cookiecutter.json").write_text(
            json.dumps(cookiecutter_json, indent=2), encoding="utf-8"
        )

    projected_context = _build_cookiecutter_context(selected_template_dir / "cookiecutter.json")
    predicted_project_dir_name = _project_dir_from_context(
        template["root_name"], projected_context
    )
    predicted_project_dir = output_dir / predicted_project_dir_name
    trace("manifest", "predicted project directory resolved", predicted_project_dir=predicted_project_dir)

    if invocation["output_dir_state"] == "existing_empty":
        output_dir.mkdir(parents=True, exist_ok=True)
        trace("manifest", "prepared existing empty output directory", output_dir=output_dir)
    elif invocation["output_dir_state"] == "project_exists":
        predicted_project_dir.mkdir(parents=True, exist_ok=True)
        (predicted_project_dir / "sentinel.txt").write_text("collision", encoding="utf-8")
        trace("manifest", "prepared existing project collision directory", predicted_project_dir=predicted_project_dir)

    replay_file = None
    if invocation["replay"] is not None:
        replay_file = workspace_dir / "replay.json"
        replay_file.write_text(json.dumps(invocation["replay"], indent=2), encoding="utf-8")
        trace("manifest", "wrote replay file", replay_file=replay_file)

    spec = ManifestExecutionSpec(
        case_id=workspace_dir.name,
        manifest_path=manifest_path.resolve(),
        workspace_dir=workspace_dir.resolve(),
        template_repo_dir=template_repo_dir.resolve(),
        output_dir=output_dir.resolve(),
        predicted_project_dir=predicted_project_dir.resolve(),
        mode=payload["mode"],
        template_source=payload["template_source"],
        invocation=InvocationConfig(
            no_input=bool(invocation["no_input"]),
            extra_context=dict(invocation["extra_context"]),
            replay=invocation["replay"],
            overwrite_if_exists=bool(invocation["overwrite_if_exists"]),
            skip_if_file_exists=bool(invocation["skip_if_file_exists"]),
            accept_hooks=bool(invocation["accept_hooks"]),
            keep_project_on_failure=bool(invocation["keep_project_on_failure"]),
            output_dir_state=str(invocation["output_dir_state"]),
        ),
        replay_file=replay_file.resolve() if replay_file else None,
        notes={"cwd": os.getcwd()},
    )
    trace("manifest", "manifest materialization complete", case_id=spec.case_id, mode=spec.mode)
    return spec
