# Tests for the Chained Hash Table implementation

import unittest
from .chained_hashing import ChainingST


class TestChainingST(unittest.TestCase):
    def setUp(self):
        self.st = ChainingST(10)  # Initialize with a small size for testing

    def test_put_and_get(self):
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
        self.st.clear()
        self.st.put('S', 1)
        self.st.put('S', 10)  # Update existing key
        self.assertEqual(self.st.get('S'), 10)

    def test_delete(self):
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


if __name__ == "__main__":
    unittest.main()
