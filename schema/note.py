def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item.get("title", "Untitled"),
        "desc": item.get("desc", ""),
        "important": item.get("important", False)
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]