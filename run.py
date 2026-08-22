from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "objective": "energy systems planning review",
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

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
