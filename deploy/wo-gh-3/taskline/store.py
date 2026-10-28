import json
from pathlib import Path

class TaskStore:
    def __init__(self, path):
        self.path = Path(path)
        self._tasks = []
        self._next_id = 1
        if self.path.exists() and self.path.read_text(encoding="utf-8").strip():
            data = json.loads(self.path.read_text(encoding="utf-8"))
            self._tasks = data.get("tasks", [])
            self._next_id = data.get("next_id", (max((t["id"] for t in self._tasks), default=0) + 1))
    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps({"tasks": self._tasks, "next_id": self._next_id}, indent=2) + "\n", encoding="utf-8")
    def add(self, title, priority="normal"):
        if title is None or not str(title).strip():
            raise ValueError("Title is required")
        task = {"id": self._next_id, "title": str(title), "priority": priority, "status": "open"}
        self._next_id += 1
        self._tasks.append(task)
        self._save()
        return dict(task)
    def list(self):
        return [dict(t) for t in self._tasks]
    def complete(self, task_id):
        for task in self._tasks:
            if task["id"] == int(task_id):
                task["status"] = "done"
                self._save()
                return dict(task)
        raise KeyError(task_id)
