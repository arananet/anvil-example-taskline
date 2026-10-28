from pathlib import Path
from .store import TaskStore

_default_store = None
def default_store():
    global _default_store
    if _default_store is None:
        _default_store = TaskStore(Path("tasks.json"))
    return _default_store

def handle(method, path, body_dict=None, store=None):
    store = store or default_store()
    body = body_dict or {}
    if method == "POST" and path == "/tasks":
        title = body.get("title")
        if not title or not str(title).strip():
            return (400, {"error": "Title is required"})
        try:
            task = store.add(title, priority=body.get("priority", "normal"))
        except ValueError as exc:
            return (400, {"error": str(exc)})
        return (201, task)
    if method == "GET" and path == "/tasks":
        return (200, {"tasks": store.list()})
    if method == "POST" and path.startswith("/tasks/") and path.endswith("/complete"):
        task_id = path.split("/")[2]
        try:
            task = store.complete(int(task_id))
        except (KeyError, ValueError):
            return (404, {"error": "Task not found"})
        return (200, task)
    return (404, {"error": "Not found"})
