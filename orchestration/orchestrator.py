from AGENTS.grid_planning_agent import run as grid
from AGENTS.generation_mix_agent import run as mix
from AGENTS.storage_agent import run as storage
from AGENTS.reliability_agent import run as reliability
from AGENTS.evidence_agent import run as evidence


def run(context):
    state = {"input": context, "stages": []}
    for name, fn in [("grid", grid), ("mix", mix), ("storage", storage), ("reliability", reliability), ("evidence", evidence)]:
        state["stages"].append({"stage": name, "output": fn(state)})
    state["status"] = "human_review_required"
    return state
