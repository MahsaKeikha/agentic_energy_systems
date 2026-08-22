"""Fail-closed governance for F88 energy systems analysis."""

BLOCKED_ACTIONS = {
    "grid_control_command",
    "dispatch_command",
    "breaker_operation",
    "protection_override",
    "autonomous_market_bid",
    "autonomous_load_shed",
}

REQUIRED_REVIEWS = (
    "grid_constraints_reviewed",
    "generation_assumptions_reviewed",
    "storage_assumptions_reviewed",
    "reliability_reviewed",
    "adequacy_reviewed",
    "stability_reviewed",
    "evidence_provenance_reviewed",
    "uncertainty_reviewed",
    "human_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in BLOCKED_ACTIONS:
        return {"allowed": False, "reason": "consequential grid execution is outside reference-system authority"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required energy-system review", "missing": missing}

    blockers = []
    if context.get("reliability_violation"):
        blockers.append("reliability criterion violated")
    if context.get("resource_adequacy_gap"):
        blockers.append("resource adequacy gap unresolved")
    if context.get("stability_limit_exceeded"):
        blockers.append("stability limit exceeded")
    if context.get("transmission_constraint_unresolved"):
        blockers.append("transmission constraint unresolved")
    if context.get("storage_model_invalid"):
        blockers.append("storage assumptions or degradation model invalid")
    if context.get("evidence_provenance_missing"):
        blockers.append("evidence provenance incomplete")
    if context.get("uncertainty_not_quantified"):
        blockers.append("material uncertainty not characterized")
    if context.get("unsupported_operational_claim"):
        blockers.append("operational claim exceeds evidence")

    if blockers:
        return {"allowed": False, "reason": "energy-system governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "analysis package approved after qualified human review"}


def require_human_review(result: dict) -> dict:
    result["status"] = "human_review_required"
    result["human_review_required"] = True
    return result
