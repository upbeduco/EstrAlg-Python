import unittest
from .red_black_st import RedBlackST, Node  # Import Node to check color if needed


class TestRedBlackSTDeletion(unittest.TestCase):
    def test_delete_on_empty_tree(self):
        """Deleting from an empty RedBlackST should leave it empty."""
        tree = RedBlackST()
        tree.delete(42)  # Should not raise
        self.assertTrue(tree.is_empty())
        self.assertEqual(tree.size(), 0)
        self.assertIsNone(tree.root)

    def test_delete_non_existing_key_one_node(self):
        """Deleting a non-existing key from a one-node RedBlackST should not change the tree."""
        tree = RedBlackST()
        tree.put(10, "ten")
        before_str = str(tree)
        tree.delete(42)  # 42 does not exist
        self.assertEqual(tree.size(), 1)
        self.assertFalse(tree.is_empty())
        self.assertEqual(tree.root.key, 10)
        self.assertEqual(tree.root.value, "ten")
        self.assertEqual(str(tree), before_str)

    def test_delete_existing_key_one_node(self):
        """Deleting the only key from a one-node RedBlackST should leave it empty."""
        tree = RedBlackST()
        tree.put(10, "ten")
        tree.delete(10)
        self.assertTrue(tree.is_empty())
        self.assertEqual(tree.size(), 0)
        self.assertIsNone(tree.root)

# TODO


if __name__ == '__main__':
    unittest.main()

