from orchestration.orchestrator import run
from safety.policy import authorize


def valid_context():
    return {
        "grid_constraints_reviewed": True,
        "generation_assumptions_reviewed": True,
        "storage_assumptions_reviewed": True,
        "reliability_reviewed": True,
        "adequacy_reviewed": True,
        "stability_reviewed": True,
        "evidence_provenance_reviewed": True,
        "uncertainty_reviewed": True,
        "human_approval": True,
    }


def test_complete_review_can_release_analysis():
    result = run(valid_context())
    assert result["release_allowed"] is True
    assert result["grid_control"] is False
    assert result["autonomous_dispatch"] is False


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert run(context)["release_allowed"] is False


def test_grid_control_command_is_never_authorized():
    assert authorize("grid_control_command", valid_context())["allowed"] is False


def test_reliability_violation_blocks_release():
    context = valid_context()
    context["reliability_violation"] = True
    assert run(context)["release_allowed"] is False


def test_resource_adequacy_gap_blocks_release():
    context = valid_context()
    context["resource_adequacy_gap"] = True
    assert run(context)["release_allowed"] is False


def test_stability_limit_blocks_release():
    context = valid_context()
    context["stability_limit_exceeded"] = True
    assert run(context)["release_allowed"] is False


def test_transmission_constraint_blocks_release():
    context = valid_context()
    context["transmission_constraint_unresolved"] = True
    assert run(context)["release_allowed"] is False


def test_storage_model_or_evidence_gap_blocks_release():
    context = valid_context()
    context["storage_model_invalid"] = True
    assert run(context)["release_allowed"] is False
