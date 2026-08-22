from AGENTS.evidence_agent import run as evidence
from AGENTS.generation_mix_agent import run as mix
from AGENTS.grid_planning_agent import run as grid
from AGENTS.reliability_agent import run as reliability
from AGENTS.storage_agent import run as storage
from safety.policy import authorize


def run(context: dict) -> dict:
    """Run energy-system specialists and apply fail-closed governance."""
    state = {"system": "F88", "input": context, "stages": []}
    for name, fn in [
        ("grid", grid),
        ("mix", mix),
        ("storage", storage),
        ("reliability", reliability),
        ("evidence", evidence),
    ]:
        state["stages"].append({"stage": name, "output": fn(state)})
    governance = authorize("analysis_release", context)
    state.update(
        {
            "status": "human_review_required",
            "human_review_required": True,
            "governance": governance,
            "release_allowed": governance["allowed"],
            "grid_control": False,
            "autonomous_dispatch": False,
        }
    )
    return state
