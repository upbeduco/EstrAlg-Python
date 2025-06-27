# Tests for the Chained Hash Table implementation

import unittest
from .chained_hashing import ChainingST


class TestChainingST(unittest.TestCase):
    def setUp(self):
        self.st = ChainingST(10)  # Initialize with a small size for testing

    def test_put_and_get(self):
        """Test inserting key-value pairs and retrieving them, including non-existent keys."""
        self.st.clear()
        self.assertIsNone(self.st.get('a'))
        self.st.put('S', 1)
        self.st.put('E', 2)
        self.st.put('A', 3)
        self.st.put('R', 4)
        self.st.put('C', 5)
        self.st.put('H', 6)
        self.st.put('M', 7)
        self.st.put('X', 8)

        self.assertEqual(self.st.get('S'), 1)
        self.assertEqual(self.st.get('E'), 2)
        self.assertEqual(self.st.get('A'), 3)
        self.assertEqual(self.st.get('R'), 4)
        self.assertEqual(self.st.get('C'), 5)
        self.assertEqual(self.st.get('H'), 6)
        self.assertEqual(self.st.get('M'), 7)
        self.assertEqual(self.st.get('X'), 8)
        self.assertIsNone(self.st.get('Z'))

    def test_put_update_existing_key(self):
        """Test updating the value of an existing key."""
        self.st.clear()
        self.st.put('S', 1)
        self.st.put('S', 10)  # Update existing key
        self.assertEqual(self.st.get('S'), 10)

    def test_delete(self):
        """Test deleting both existing and non-existing keys."""
        self.st.clear()
        keys_values = {'S':1, 'E':2, 'A':3, 'R':4, 'C':5, 'H':6, 'M':7, 'X':8}
        for k,v in keys_values.items():
            self.st.put(k,v)

        initial_size = len(keys_values)

        # Test deleting a non-existing key
        self.st.delete('Z')
        for k in keys_values:
            self.assertEqual(self.st.get(k), keys_values[k])

        # Test deleting an existing key
        self.st.delete('S')
        del keys_values['S']
        for k in keys_values:
            self.assertEqual(self.st.get(k), keys_values[k])
        
    def test_rehashing(self):
        """Test rehashing the table to a new size and ensure all data is preserved."""
        self.st.clear()
        # Rehashing should not lose any data
        for i in range(25):
            self.st.put(f'key{i}', i)
    
        # print(str(self.st))
        new_size = 15
        self.st.rehash(new_size)
        # print(str(self.st))

        self.assertEqual(len(self.st), 25)  # Ensure all items are still present
        for i in range(25):
            self.assertEqual(self.st.get(f'key{i}'), i)
            self.assertTrue(f'key{i}' in self.st)

    def test_collision_handling(self):
        """Test that different keys with the same hash index (collision) are both stored and retrievable."""
        self.st.clear()
        # Force collision by using keys with same hash modulo M
        class KeyWithHash:
            def __init__(self, value, forced_hash):
                self.value = value
                self._hash = forced_hash
            def __hash__(self):
                return self._hash
            def __eq__(self, other):
                return isinstance(other, KeyWithHash) and self.value == other.value
            def __repr__(self):
                return f"KeyWithHash({self.value})"
        k1 = KeyWithHash('a', 1)
        k2 = KeyWithHash('b', 1)  # Same hash as k1
        self.st.put(k1, 100)
        self.st.put(k2, 200)
        self.assertEqual(self.st.get(k1), 100)
        self.assertEqual(self.st.get(k2), 200)
        self.st.delete(k1)
        self.assertIsNone(self.st.get(k1))
        self.assertEqual(self.st.get(k2), 200)

    def test_contains(self):
        """Test the __contains__ method (the 'in' operator) for present and absent keys."""
        self.st.clear()
        self.st.put('foo', 123)
        self.assertIn('foo', self.st)
        self.assertNotIn('bar', self.st)

    def test_keys(self):
        """Test that keys() returns all inserted keys."""
        self.st.clear()
        keys = ['a', 'b', 'c']
        for i, k in enumerate(keys):
            self.st.put(k, i)
        returned_keys = self.st.keys()
        for k in keys:
            self.assertIn(k, returned_keys)
        self.assertEqual(set(returned_keys), set(keys))

    def test_clear(self):
        """Test that clear() empties the table and all gets return None."""
        self.st.put('x', 1)
        self.st.put('y', 2)
        self.st.clear()
        self.assertEqual(len(self.st), 0)
        self.assertIsNone(self.st.get('x'))
        self.assertIsNone(self.st.get('y'))
        self.assertEqual(self.st.keys(), [])

    def test_len(self):
        """Test that __len__ returns the correct number of key-value pairs after insertions and deletions."""
        self.st.clear()
        self.assertEqual(len(self.st), 0)
        self.st.put('a', 1)
        self.assertEqual(len(self.st), 1)
        self.st.put('b', 2)
        self.assertEqual(len(self.st), 2)
        self.st.delete('a')
        self.assertEqual(len(self.st), 1)
        self.st.delete('b')
        self.assertEqual(len(self.st), 0)

    def test_delete_all_in_bucket(self):
        """Test that deleting all keys in a bucket (with collisions) leaves the bucket empty."""
        self.st.clear()
        # Use custom keys to force collision
        class KeyWithHash:
            def __init__(self, value, forced_hash):
                self.value = value
                self._hash = forced_hash
            def __hash__(self):
                return self._hash
            def __eq__(self, other):
                return isinstance(other, KeyWithHash) and self.value == other.value
        k1 = KeyWithHash('a', 2)
        k2 = KeyWithHash('b', 2)
        self.st.put(k1, 1)
        self.st.put(k2, 2)
        self.st.delete(k1)
        self.st.delete(k2)
        # The bucket at index 2 should be empty
        self.assertEqual(self.st.st[2], [])


if __name__ == "__main__":
    unittest.main()
