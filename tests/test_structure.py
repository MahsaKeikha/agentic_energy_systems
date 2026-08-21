from pathlib import Path


def test_reference_structure():
    root = Path(__file__).resolve().parents[1]
    for folder in ["AGENTS","TOOLS","SKILLS","orchestration","memory","state","schemas","prompts","config","safety","observability","evals","benchmarks","examples","docs"]:
        assert (root / folder).exists()
    assert len(list((root / "AGENTS").glob("*_agent.py"))) >= 5
    assert len(list((root / "TOOLS").glob("*.py"))) >= 5
    assert len(list((root / "SKILLS").glob("*.py"))) >= 5
