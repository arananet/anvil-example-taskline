import tempfile, unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from taskline.store import TaskStore
from taskline.api import handle

class TasklineTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.file = Path(self.tmp.name) / "tasks.json"
        self.store = TaskStore(self.file)
    def tearDown(self):
        self.tmp.cleanup()
    def test_s1_create_returns_201_with_id_and_open(self):
        """S1 create task returns 201 with id and status open"""
        status, body = handle("POST", "/tasks", {"title": "Write spec"}, store=self.store)
        self.assertEqual(status, 201)
        self.assertIn("id", body)
        self.assertEqual(body["status"], "open")
    def test_s2_list_returns_all_created(self):
        """S2 list tasks returns all created tasks"""
        handle("POST", "/tasks", {"title": "One"}, store=self.store)
        handle("POST", "/tasks", {"title": "Two"}, store=self.store)
        status, body = handle("GET", "/tasks", None, store=self.store)
        self.assertEqual(status, 200)
        self.assertEqual(len(body["tasks"]), 2)
    def test_s3_complete_marks_done(self):
        """S3 complete task marks it done"""
        _, created = handle("POST", "/tasks", {"title": "Finish"}, store=self.store)
        status, body = handle("POST", f"/tasks/{created['id']}/complete", None, store=self.store)
        self.assertEqual(status, 200)
        self.assertEqual(body["status"], "done")
    def test_s4_complete_missing_returns_404(self):
        """S4 completing a missing task returns 404"""
        status, _ = handle("POST", "/tasks/999/complete", None, store=self.store)
        self.assertEqual(status, 404)
    def test_s5_create_without_title_returns_400(self):
        """S5 creating a task without a title returns 400"""
        # Missing title key
        status, _ = handle("POST", "/tasks", {}, store=self.store)
        self.assertEqual(status, 400)
        # Empty title string through API
        status, _ = handle("POST", "/tasks", {"title": ""}, store=self.store)
        self.assertEqual(status, 400)
        # Whitespace-only title through API
        status, _ = handle("POST", "/tasks", {"title": "  "}, store=self.store)
        self.assertEqual(status, 400)
        # Store level validation
        with self.assertRaises(ValueError):
            self.store.add("")
    def test_s6_persistence_survives_reload(self):
        """S6 tasks persist to a JSON file and survive a reload"""
        self.store.add("Persist me")
        reloaded = TaskStore(self.file)
        titles = [t["title"] for t in reloaded.list()]
        self.assertIn("Persist me", titles)

if __name__ == "__main__":
    unittest.main()
