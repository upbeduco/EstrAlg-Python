import unittest
import random
from .binary_heap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):
    def setUp(self):
        self.heap = BinaryHeap()

    def test_empty(self):
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 0)
        self.assertEqual(len(self.heap), 0)
        self.assertEqual(str(self.heap), "[]")
        self.assertEqual(list(self.heap), [])
        self.assertEqual(self.heap.max(), None)
        self.assertEqual(self.heap.del_max(), None)

    def test_insert(self):
        self.heap.insert(1)
        self.assertEqual(self.heap.max(), 1)
        self.heap.insert(2)
        self.assertEqual(self.heap.max(), 2)

    def test_del_max(self):
        self.heap.clear()
        for i in range(20):
            self.heap.insert(i)

        for i in range(19, -1, -1):
            self.assertEqual(self.heap.del_max(), i)
            self.assertEqual(self.heap.max(), i-1 if i > 0 else None)

        # The heap should be empty now
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 0)
        self.assertEqual(len(self.heap), 0)
        self.assertEqual(str(self.heap), "[]")
        self.assertEqual(list(self.heap), [])
        self.assertEqual(self.heap.max(), None)
        self.assertEqual(self.heap.del_max(), None)


    def test_del_max_random(self):
        self.heap.clear()
        keys = [random.randint(0, 100) for _ in range(20)]
        # print(f"Random keys: {keys}")
        for key in keys:
            self.heap.insert(key)

        sorted_keys = sorted(keys, reverse=True)
        # print(f"Sorted keys: {sorted_keys}")
        for i in range(20):
            key = self.heap.del_max()
            self.assertEqual(key, sorted_keys[i])
            self.assertEqual(self.heap.max(), sorted_keys[i+1] if i < 19 else None)

        # The heap should be empty now
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 0)
        self.assertEqual(len(self.heap), 0)
        self.assertEqual(str(self.heap), "[]")
        self.assertEqual(list(self.heap), [])
        self.assertEqual(self.heap.max(), None)
        self.assertEqual(self.heap.del_max(), None)

    def test_clear(self):
        for i in range(10):
            self.heap.insert(i)
        self.assertFalse(self.heap.is_empty())
        self.heap.clear()
        self.assertTrue(self.heap.is_empty())
        self.assertEqual(self.heap.size(), 0)
        self.assertEqual(len(self.heap), 0)
        self.assertEqual(str(self.heap), "[]")
        self.assertEqual(list(self.heap), [])
        self.assertEqual(self.heap.max(), None)
        self.assertEqual(self.heap.del_max(), None)

    def test_union(self):
        heap1 = BinaryHeap()
        heap2 = BinaryHeap()

        for i in range(10):
            heap1.insert(i)
        for i in range(5, 15):
            heap2.insert(i)

        # Union of two heaps
        heap1.union(heap2)

        # Check the max value after union
        self.assertEqual(heap1.max(), 14)

        # Check the size after union
        self.assertEqual(heap1.size(), 20)

        # Check if all elements are present
        expected_elements = set(range(15))
        actual_elements = set(heap1)
        self.assertEqual(expected_elements, actual_elements)

        


if __name__ == "__main__":
    unittest.main()