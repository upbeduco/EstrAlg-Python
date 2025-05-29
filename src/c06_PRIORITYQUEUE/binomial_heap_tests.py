import unittest
import random
from .binomial_heap import BinomialHeap

class TestBinomialHeap(unittest.TestCase):
    def setUp(self):
        self.heap = BinomialHeap()

    def test_empty(self):
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 0)
        self.assertEqual(str(self.heap), "BinomialHeap()")
        self.assertEqual(self.heap.max(), None)
        self.assertEqual(self.heap.del_max(), None)

    def test_insert(self):
        self.heap.insert(1)
        self.assertEqual(self.heap.max(), 1)
        self.assertFalse(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 1)
        self.heap.insert(2)
        self.assertEqual(self.heap.max(), 2)
        self.assertEqual(self.heap.size(), 2)

    def test_del_max(self):
        self.heap.clear()
        for i in range(20):
            self.heap.insert(i)
        for i in range(19, -1, -1):
            self.assertEqual(self.heap.del_max(), i)
            self.assertEqual(self.heap.max(), i-1 if i > 0 else None)
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 0)
        self.assertEqual(str(self.heap), "BinomialHeap()")
        self.assertEqual(self.heap.max(), None)
        self.assertEqual(self.heap.del_max(), None)

    def test_del_max_random(self):
        import random
        self.heap.clear()
        keys = [random.randint(0, 100) for _ in range(20)]
        for key in keys:
            self.heap.insert(key)
        sorted_keys = sorted(keys, reverse=True)
        for i in range(20):
            key = self.heap.del_max()
            self.assertEqual(key, sorted_keys[i])
            self.assertEqual(self.heap.max(), sorted_keys[i+1] if i < 19 else None)
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 0)
        self.assertEqual(str(self.heap), "BinomialHeap()")
        self.assertEqual(self.heap.max(), None)
        self.assertEqual(self.heap.del_max(), None)

    def test_clear(self):
        for i in range(10):
            self.heap.insert(i)
        self.assertFalse(self.heap.is_empty())
        self.heap.clear()
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 0)
        self.assertEqual(self.heap.max(), None)
        self.assertEqual(self.heap.del_max(), None)

    def test_union(self):
        heap1 = BinomialHeap()
        heap2 = BinomialHeap()
        for i in range(5):
            heap1.insert(i)
        for i in range(5, 10):
            heap2.insert(i)
        heap1.union(heap2)
        self.assertEqual(heap1.size(), 10)
        self.assertEqual(heap1.max(), 9)

        # Test union with an empty heap
        empty_heap = BinomialHeap()
        heap1.union(empty_heap)
        self.assertEqual(heap1.size(), 10)
        self.assertEqual(heap1.max(), 9)

    def test_pythonic_operators(self):
        """Test the len(), str(), contains() methods"""
        self.heap.clear()
        self.assertEqual(len(self.heap), 0)
        self.assertEqual(str(self.heap), "BinomialHeap()")
        self.assertNotIn(5, self.heap)
        for i in range(3):
            self.heap.insert(i)
        self.assertEqual(len(self.heap), 3)
        self.assertIn(0, self.heap)
        self.assertIn(1, self.heap)
        self.assertIn(2, self.heap)
        self.assertNotIn(5, self.heap)
        self.assertTrue(str(self.heap).startswith("BinomialHeap"))

    def test_iter(self):
        """Test the iterator functionality"""
        self.heap.clear()
        self.assertEqual(list(self.heap), [])
        keys = [random.randint(0, 100) for _ in range(20)]
        for key in keys:
            self.heap.insert(key)
        self.assertEqual(len(self.heap), 20)
        iterated_keys = list(self.heap)
        self.assertEqual(len(iterated_keys), 20)
        self.assertEqual(set(iterated_keys), set(sorted(keys, reverse=True)))


if __name__ == "__main__":
    unittest.main()


