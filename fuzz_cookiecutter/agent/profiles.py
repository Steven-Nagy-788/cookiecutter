from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SandboxProfile:
    name: str
    uses_docker: bool
    description: str


DOCKER_PROFILE = SandboxProfile(
    name="docker",
    uses_docker=True,
    description="Run each case inside Docker when available.",
)

SUBPROCESS_PROFILE = SandboxProfile(
    name="subprocess",
    uses_docker=False,
    description="Run each case in a separate Python subprocess inside the workspace.",
)


def get_profile(name: str) -> SandboxProfile:
    normalized = name.strip().lower()
    if normalized == "docker":
        return DOCKER_PROFILE
    return SUBPROCESS_PROFILE

