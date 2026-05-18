from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests


@dataclass(slots=True)
class ChatResponse:
    provider: str
    text: str


class BaseLLMClient:
    def complete(self, prompt: str, purpose: str) -> ChatResponse:
        raise NotImplementedError


class OpenAICompatibleLLMClient(BaseLLMClient):
    def __init__(
        self,
        *,
        base_url: str,
        api_key: str,
        model_name: str,
        timeout_seconds: int,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.model_name = model_name
        self.timeout_seconds = timeout_seconds

    def complete(self, prompt: str, purpose: str) -> ChatResponse:
        url = f"{self.base_url}/chat/completions"
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": self.model_name,
                "temperature": 0.1,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=self.timeout_seconds,
        )
        response.raise_for_status()
        payload = response.json()
        content = payload["choices"][0]["message"]["content"]
        return ChatResponse(provider="openai-compatible", text=content)


import random

class HeuristicLLMClient(BaseLLMClient):
    def complete(self, prompt: str, purpose: str) -> ChatResponse:
        if purpose == "planner":
            payload: dict[str, Any] = {
                "analysis": "Heuristic fallback planner. Exploring CLI args and JSON keys.",
                "overrepresented_responses": [],
                "underexplored_scenario_families": ["cli options", "json keys"],
                "reachable_by_grammar": ["add more cli options", "add malicious json strings"],
                "reachable_by_harness_only": [],
                "unreachable_harness_limits": [],
                "line_target_hints": [],
                "recommended_rule_edits": [
                    {
                        "rule": "render_item",
                        "rationale": "Add more CLI flags.",
                    },
                    {
                        "rule": "key",
                        "rationale": "Add missing cookiecutter dict keys.",
                    }
                ],
            }
            return ChatResponse(provider="heuristic", text=json.dumps(payload, indent=2))

        # We randomly pick one of the rules to modify so it evolves over iterations
        rules = [
            {
                "rule": "render_item",
                "replacement": (
                    "render_item\n"
                    "    : DEFAULT_CONFIG | VALID_CONFIG | PARTIAL_CONFIG | OVERWRITE | SKIP "
                    "| KEEP | VERBOSE | ACCEPT_YES | ACCEPT_NO | EXTRA_REPO_NAME | EXTRA_PROJECT_NAME "
                    "| EXTRA_SHORT_DESC | EXTRA_FULL_NAME | EXTRA_EMAIL | EXTRA_GITHUB "
                    "| '--debug' | '-V' | '-h' | '--no-input' | '--replay' | '--checkout' SPACE IDENT\n"
                    "    ;"
                )
            },
            {
                "rule": "template",
                "replacement": (
                    "template\n"
                    "    : FAKE_REPO_PRE | FAKE_REPO_TMPL | FAKE_REPO_DICT "
                    "| 'tests/fake-repo/' | 'tests/fake-repo-bad/' | 'tests/test-extensions/' | 'tests/test-hooks/'\n"
                    "    ;"
                )
            },
            {
                "rule": "key",
                "replacement": (
                    "key\n"
                    "    : PROJECT_NAME | PROJECT_SLUG | DESCRIPTION | FULL_NAME | EMAIL | VERSION "
                    "| LICENSE | REPO_NAME | MODULE_NAME | COPY_WITHOUT_RENDER | JINJA2_ENV_VARS | EXTENSIONS "
                    "| NEW_LINES | PROMPTS | TEMPLATE | TEMPLATES | IDENT "
                    "| '_template' | '_output_dir' | '_repo_dir' | '_requirements'\n"
                    "    ;"
                )
            },
            {
                "rule": "SAFE_NAME",
                "replacement": (
                    "SAFE_NAME\n"
                    "    : 'safe_default' | 'baseline_project' | 'test_project' "
                    "| 'test_'+ IDENT | '{{cookiecutter.project_slug}}' | 'malicious_'+ IDENT\n"
                    "    ;"
                )
            }
        ]

        payload = {
            "rationale": "Heuristic fallback injecting new random options to increase coverage.",
            "updates": [random.choice(rules)],
        }
        return ChatResponse(provider="heuristic", text=json.dumps(payload, indent=2))


class FallbackChainLLMClient(BaseLLMClient):
    def __init__(self, primary: BaseLLMClient, fallback: BaseLLMClient) -> None:
        self.primary = primary
        self.fallback = fallback

    def complete(self, prompt: str, purpose: str) -> ChatResponse:
        try:
            return self.primary.complete(prompt, purpose)
        except Exception:  # noqa: BLE001
            return self.fallback.complete(prompt, purpose)


def build_llm_client(
    *, base_url: str | None, api_key: str | None, model_name: str, timeout_seconds: int
) -> BaseLLMClient:
    fallback = HeuristicLLMClient()
    if base_url and api_key:
        return FallbackChainLLMClient(
            primary=OpenAICompatibleLLMClient(
                base_url=base_url,
                api_key=api_key,
                model_name=model_name,
                timeout_seconds=timeout_seconds,
            ),
            fallback=fallback,
        )
    return fallback


def load_dotenv_files(*paths: Path) -> None:
    for path in paths:
        if not path.exists():
            continue
        for raw_line in path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())
