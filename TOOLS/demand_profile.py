def summarize(values):
    return {"count": len(values), "peak": max(values) if values else None}
