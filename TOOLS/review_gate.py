def require(approved=False):
    return {"approved": bool(approved), "status": "approved" if approved else "human_review_required"}
