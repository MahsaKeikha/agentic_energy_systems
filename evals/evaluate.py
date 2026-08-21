def evaluate(result):
    return {"passed": len(result.get("stages", [])) >= 5 and result.get("status") == "human_review_required"}
