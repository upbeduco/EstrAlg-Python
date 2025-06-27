# To run:
# PYTHONPATH=src python3 -m c07_SEARCH.BinarySearch_tests

import unittest
from c07_SEARCH.BinarySearch import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.bs = BinarySearch()

    def test_empty(self):
        self.assertTrue(self.bs.is_empty())
        self.assertEqual(self.bs.size(), 0)
        self.assertIsNone(self.bs.get("a"))
        self.assertFalse(self.bs.contains("a"))
        self.assertIsNone(self.bs.min())
        self.assertIsNone(self.bs.max())
        self.assertIsNone(self.bs.select(0))

    def test_put_and_get(self):
        self.bs.put("a", 1)
        self.assertFalse(self.bs.is_empty())
        self.assertEqual(self.bs.size(), 1)
        self.assertEqual(self.bs.get("a"), 1)
        self.assertTrue(self.bs.contains("a"))

        self.bs.put("b", 2)
        self.bs.put("c", 3)
        self.assertEqual(self.bs.size(), 3)
        self.assertEqual(self.bs.get("b"), 2)
        self.assertEqual(self.bs.get("c"), 3)

    def test_update(self):
        self.bs.put("a", 1)
        self.bs.put("a", 10)
        self.assertEqual(self.bs.get("a"), 10)
        self.assertEqual(self.bs.size(), 1)

    def test_delete(self):
        self.bs.put("a", 1)
        self.bs.put("b", 2)
        self.bs.put("c", 3)
        self.bs.delete("b")
        self.assertEqual(self.bs.size(), 2)
        self.assertFalse(self.bs.contains("b"))
        self.assertIsNone(self.bs.get("b"))
        self.bs.delete("a")
        self.bs.delete("c")
        self.assertTrue(self.bs.is_empty())
        self.assertEqual(self.bs.size(), 0)

    def test_delete_nonexistent(self):
        self.bs.put("a", 1)
        self.bs.delete("b")  # Should not raise
        self.assertEqual(self.bs.size(), 1)
        self.bs.delete("a")
        self.bs.delete("a")  # Should not raise
        self.assertEqual(self.bs.size(), 0)

    def test_min_max_select(self):
        keys = ["d", "b", "a", "c"]
        for i, k in enumerate(keys):
            self.bs.put(k, i)
        self.assertEqual(self.bs.min(), "a")
        self.assertEqual(self.bs.max(), "d")
        self.assertEqual(self.bs.select(0), "a")
        self.assertEqual(self.bs.select(1), "b")
        self.assertEqual(self.bs.select(2), "c")
        self.assertEqual(self.bs.select(3), "d")
        self.assertIsNone(self.bs.select(-1))
        self.assertIsNone(self.bs.select(4))

if __name__ == "__main__":
    unittest.main() 