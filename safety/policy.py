def require_human_review(result):
    result["status"] = "human_review_required"
    return result
