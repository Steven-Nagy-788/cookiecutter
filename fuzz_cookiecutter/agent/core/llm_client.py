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


class HeuristicLLMClient(BaseLLMClient):
    def complete(self, prompt: str, purpose: str) -> ChatResponse:
        if purpose == "planner":
            payload: dict[str, Any] = {
                "analysis": (
                    "Baseline-only heuristic planner output. The harness is configured "
                    "to prefer local template cases, hook outcomes, replay paths, and "
                    "output collisions."
                ),
                "overrepresented_responses": ["simple no_input local template success"],
                "underexplored_scenario_families": [
                    "hook failure cases",
                    "replay-driven cases",
                    "nested template menu cases",
                ],
                "reachable_by_grammar": [
                    "Add more hook body variants",
                    "Broaden replay payload diversity",
                ],
                "reachable_by_harness_only": [
                    "Docker-only isolation behavior",
                ],
                "unreachable_harness_limits": [],
                "line_target_hints": [
                    {
                        "target": "cookiecutter/hooks.py:130",
                        "delivery": "grammar",
                        "code_signal": "run hook paths with both success and failure outcomes",
                        "required_inputs": "pre/post hook script bodies and accept_hooks enabled",
                        "grammar_implication": "broaden hook_script alternatives",
                    }
                ],
                "recommended_rule_edits": [
                    {
                        "rule": "hook_script",
                        "rationale": "Hook bodies are a direct route into hook execution branches.",
                    }
                ],
            }
            return ChatResponse(provider="heuristic", text=json.dumps(payload, indent=2))

        payload = {
            "rationale": "Heuristic fallback keeps the grammar stable for smoke runs.",
            "updates": [
                {
                    "rule": "hook_script",
                    "replacement": (
                        "hook_script\n"
                        "    : 'null'\n"
                        "    | '\"from pathlib import Path\\\\nPath(\\'HOOK_OK\\').write_text(\\'ok\\', encoding=\\'utf-8\\')\\\\n\"'\n"
                        "    | '\"raise SystemExit(1)\\\\n\"'\n"
                        "    ;"
                    ),
                }
            ],
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
