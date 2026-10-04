"""Regression checks use an in-process client; no network listener is started."""
import unittest
from app import app

class LessonSearchTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_git_topic(self):
        self.assertEqual(self.client.get("/lessons?topic=Git").get_json(), ["First commit"])

    def test_actions_topic(self):
        self.assertEqual(self.client.get("/lessons?topic=Actions").get_json(), ["First workflow"])

    def test_unknown_topic(self):
        self.assertEqual(self.client.get("/lessons?topic=Unknown").get_json(), [])

    def test_query_text_is_data(self):
        response = self.client.get("/lessons", query_string={"topic": "' OR '1'='1"})
        self.assertEqual(response.get_json(), [])

if __name__ == "__main__":
    unittest.main(verbosity=2)
