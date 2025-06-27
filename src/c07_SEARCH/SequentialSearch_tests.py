# To run:
# PYTHONPATH=src python3 -m c07_SEARCH.SequentialSearch_tests

import unittest
from c07_SEARCH.SequentialSearch import SequentialSearch

class TestSequentialSearch(unittest.TestCase):
    def setUp(self):
        self.ss = SequentialSearch()

    def test_empty(self):
        self.assertTrue(self.ss.is_empty())
        self.assertEqual(self.ss.size(), 0)
        self.assertIsNone(self.ss.get("a"))
        self.assertFalse(self.ss.contains("a"))

    def test_put_and_get(self):
        self.ss.put("a", 1)
        self.assertFalse(self.ss.is_empty())
        self.assertEqual(self.ss.size(), 1)
        self.assertEqual(self.ss.get("a"), 1)
        self.assertTrue(self.ss.contains("a"))

        self.ss.put("b", 2)
        self.ss.put("c", 3)
        self.assertEqual(self.ss.size(), 3)
        self.assertEqual(self.ss.get("b"), 2)
        self.assertEqual(self.ss.get("c"), 3)

    def test_update(self):
        self.ss.put("a", 1)
        self.ss.put("a", 10)
        self.assertEqual(self.ss.get("a"), 10)
        self.assertEqual(self.ss.size(), 1)

    def test_delete(self):
        self.ss.put("a", 1)
        self.ss.put("b", 2)
        self.ss.put("c", 3)
        self.ss.delete("b")
        self.assertEqual(self.ss.size(), 2)
        self.assertFalse(self.ss.contains("b"))
        self.assertIsNone(self.ss.get("b"))
        self.ss.delete("a")
        self.ss.delete("c")
        self.assertTrue(self.ss.is_empty())
        self.assertEqual(self.ss.size(), 0)

    def test_delete_nonexistent(self):
        self.ss.put("a", 1)
        self.ss.delete("b")  # Should not raise
        self.assertEqual(self.ss.size(), 1)
        self.ss.delete("a")
        self.ss.delete("a")  # Should not raise
        self.assertEqual(self.ss.size(), 0)

if __name__ == "__main__":
    unittest.main() 