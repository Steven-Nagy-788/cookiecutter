from __future__ import annotations

import re
import shutil
import tempfile
from pathlib import Path

from fuzz_cookiecutter.agent.core.config import FuzzerConfig
from fuzz_cookiecutter.agent.utils.cli_utils import run_command
from fuzz_cookiecutter.agent.utils.monitoring import trace


def grammar_name(grammar_path: Path) -> str:
    trace("grammar", "reading grammar declaration", path=grammar_path)
    match = re.search(
        r"grammar\s+([A-Za-z_][A-Za-z0-9_]*)\s*;",
        grammar_path.read_text(encoding="utf-8"),
    )
    if not match:
        msg = f"Could not determine grammar name from {grammar_path}"
        raise ValueError(msg)
    return match.group(1)


def process_grammar(config: FuzzerConfig, grammar_path: Path, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    trace("grammar", "running grammarinator-process", grammar_path=grammar_path, output_dir=output_dir)
    result = run_command(
        ["grammarinator-process", str(grammar_path), "-o", str(output_dir)],
        cwd=config.repo_root,
    )
    if result.returncode != 0:
        msg = result.stderr.strip() or result.stdout.strip() or "unknown error"
        trace("grammar", "grammarinator-process failed", error=msg)
        raise RuntimeError(f"grammarinator-process failed: {msg}")
    name = grammar_name(grammar_path)
    generator = output_dir / f"{name}Generator.py"
    if not generator.exists():
        matches = sorted(output_dir.glob("*Generator.py"))
        if not matches:
            trace("grammar", "no generator emitted", output_dir=output_dir)
            raise RuntimeError(f"No generator emitted into {output_dir}")
        generator = matches[0]
    trace("grammar", "grammarinator-process finished", generator=generator)
    return generator


def generate_cases(
    config: FuzzerConfig,
    generator_path: Path,
    *,
    case_count: int,
    depth: int,
    output_dir: Path,
) -> list[Path]:
    if output_dir.exists():
        shutil.rmtree(output_dir)
        trace("grammar", "removed previous generated cases directory", path=output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    module_class = f"{generator_path.stem}.{generator_path.stem}"
    pattern = str(output_dir / "case_%d.json")
    trace("grammar", "running grammarinator-generate", module=module_class, count=case_count, depth=depth, output_pattern=pattern)
    result = run_command(
        [
            "grammarinator-generate",
            module_class,
            "-r",
            "start",
            "-n",
            str(case_count),
            "-d",
            str(depth),
            "--sys-path",
            str(generator_path.parent),
            "-o",
            pattern,
        ],
        cwd=config.repo_root,
    )
    if result.returncode != 0:
        msg = result.stderr.strip() or result.stdout.strip() or "unknown error"
        trace("grammar", "grammarinator-generate failed", error=msg)
        raise RuntimeError(f"grammarinator-generate failed: {msg}")
    manifests = sorted(
        output_dir.glob("case_*.json"),
        key=lambda item: int(item.stem.split("_")[1]),
    )
    if not manifests:
        trace("grammar", "no manifests generated", output_dir=output_dir)
        raise RuntimeError(f"No manifests generated into {output_dir}")
    trace("grammar", "grammarinator-generate finished", manifest_count=len(manifests))
    return manifests


def compile_candidate_smoke(config: FuzzerConfig, candidate_grammar: str) -> tuple[bool, str]:
    trace("validator", "starting candidate grammar smoke compilation")
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_root = Path(temp_dir)
        grammar_path = temp_root / config.grammar_path.name
        generator_dir = temp_root / "gen"
        grammar_path.write_text(candidate_grammar, encoding="utf-8")
        try:
            generator = process_grammar(config, grammar_path, generator_dir)
            generated = generate_cases(
                config,
                generator,
                case_count=1,
                depth=max(4, config.generation_depth // 2),
                output_dir=temp_root / "cases",
            )
        except Exception as exc:
            trace("validator", "candidate smoke compilation failed", error=exc)
            return False, str(exc)
        sample = generated[0].read_text(encoding="utf-8").strip()
        if not sample.startswith("{"):
            trace("validator", "candidate smoke sample invalid", sample_preview=sample[:80])
            return False, "Generated smoke sample is not a JSON object"
    trace("validator", "candidate grammar smoke compilation passed")
    return True, "ok"
