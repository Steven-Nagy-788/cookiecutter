from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _env_int(name: str, default: int) -> int:
    value = os.environ.get(name)
    if value is None:
        return default
    return int(value)


@dataclass(slots=True)
class FuzzerConfig:
    repo_root: Path
    package_dir: Path
    grammar_path: Path
    cases_dir: Path
    generated_dir: Path
    baselines_dir: Path
    findings_dir: Path
    history_dir: Path
    logs_dir: Path
    reports_dir: Path
    run_cache_dir: Path
    coverage_json_path: Path
    batch_size: int
    generation_depth: int
    per_case_timeout_seconds: int
    max_iterations: int
    mutation_retry_limit: int
    sandbox_mode: str
    llm_model_name: str
    llm_base_url: str | None
    llm_api_key: str | None
    llm_timeout_seconds: int

    @classmethod
    def discover(cls, repo_root: Path | None = None) -> "FuzzerConfig":
        root = (repo_root or Path(__file__).resolve().parents[3]).resolve()
        package_dir = root / "fuzz_cookiecutter"
        return cls(
            repo_root=root,
            package_dir=package_dir,
            grammar_path=package_dir / "cookiecutter_case.g4",
            cases_dir=package_dir / "generator" / "test-cases",
            generated_dir=package_dir / "generator" / "generated",
            baselines_dir=package_dir / "baselines",
            findings_dir=package_dir / "findings",
            history_dir=package_dir / "history",
            logs_dir=package_dir / "logs",
            reports_dir=package_dir / "reports",
            run_cache_dir=package_dir / "run_cache",
            coverage_json_path=package_dir / "coverage.json",
            batch_size=_env_int("FUZZ_COOKIECUTTER_BATCH_SIZE", 12),
            generation_depth=_env_int("FUZZ_COOKIECUTTER_GENERATION_DEPTH", 12),
            per_case_timeout_seconds=_env_int("FUZZ_COOKIECUTTER_TIMEOUT", 20),
            max_iterations=_env_int("FUZZ_COOKIECUTTER_ITERATIONS", 1),
            mutation_retry_limit=_env_int("FUZZ_COOKIECUTTER_MUTATION_RETRIES", 2),
            sandbox_mode=os.environ.get("FUZZ_COOKIECUTTER_SANDBOX", "subprocess"),
            llm_model_name=os.environ.get(
                "LLM_MODEL_NAME", "gpt-4.1-mini"
            ),
            llm_base_url=os.environ.get("LLM_BASE_URL"),
            llm_api_key=os.environ.get("LLM_API_KEY"),
            llm_timeout_seconds=_env_int("FUZZ_COOKIECUTTER_LLM_TIMEOUT", 15),
        )

    def ensure_directories(self) -> None:
        for path in (
            self.cases_dir,
            self.generated_dir,
            self.baselines_dir,
            self.findings_dir,
            self.history_dir,
            self.logs_dir,
            self.reports_dir,
            self.run_cache_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)
