from orchestration.orchestrator import run


def base():
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "reliability_violation": True}, False),
    ({**base(), "resource_adequacy_gap": True}, False),
    ({**base(), "stability_limit_exceeded": True}, False),
    ({**base(), "transmission_constraint_unresolved": True}, False),
    ({**base(), "storage_model_invalid": True}, False),
    ({**base(), "evidence_provenance_missing": True}, False),
    ({**base(), "uncertainty_not_quantified": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
