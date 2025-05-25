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

    def test_delete_left_child(self):
        """Delete the left child from a three-node tree and verify postconditions."""
        tree = RedBlackST()
        tree.put(10, "root")
        tree.put(5, "left")
        tree.put(15, "right")
        tree.delete(5)
        self.assertEqual(tree.size(), 2)
        self.assertIn(10, tree)
        self.assertIn(15, tree)
        self.assertNotIn(5, tree)
        self.assertIn(tree.root.key, [10, 15])
        self.assertNotIn(5, tree)
        # self.assertEqual(set(tree.keys()), {10, 15})

    def test_delete_right_child(self):
        """Delete the right child from a three-node tree and verify postconditions."""
        tree = RedBlackST()
        tree.put(10, "root")
        tree.put(5, "left")
        tree.put(15, "right")
        tree.delete(15)
        self.assertEqual(tree.size(), 2)

    def test_delete_all_nodes_one_by_one(self):
        """Delete all nodes one by one and ensure the tree is empty at the end."""
        tree = RedBlackST()
        tree.put(10, "root")
        tree.put(5, "left")
        tree.put(15, "right")
        tree.delete(5)
        self.assertEqual(tree.size(), 2)
        tree.delete(15)
        self.assertEqual(tree.size(), 1)
        tree.delete(10)
        self.assertTrue(tree.is_empty())
        self.assertEqual(tree.size(), 0)
        self.assertIsNone(tree.root)

    def test_delete_non_existing_key_multiple_nodes(self):
        """Deleting a non-existing key from a multi-node RedBlackST should not change the tree."""
        tree = RedBlackST()
        tree.put(10, "root")
        tree.put(5, "left")
        tree.put(15, "right")
        before = [tree.root.key, tree.root.left.key if tree.root.left else None, tree.root.right.key if tree.root.right else None]
        tree.delete(99)  # 99 does not exist
        after = [tree.root.key, tree.root.left.key if tree.root.left else None, tree.root.right.key if tree.root.right else None]
        self.assertEqual(before, after)
        self.assertEqual(tree.size(), 3)

    def test_delete_from_larger_tree(self):
        """Delete a node from a larger tree and check structure and size."""
        tree = RedBlackST()
        for k in [20, 10, 30, 5, 15, 25, 35]:
            tree.put(k, str(k))
        tree.delete(10)
        self.assertEqual(tree.size(), 6)
        self.assertNotIn(10, tree)
        # Check all other keys are still present
        for k in [20, 5, 15, 25, 30, 35]:
            self.assertIn(k, tree)

    def test_delete_minimum(self):
        """Delete the minimum key and check the new minimum."""
        tree = RedBlackST()
        for k in [10, 5, 15, 2]:
            tree.put(k, str(k))
        tree.delete(2)
        self.assertEqual(tree.size(), 3)
        self.assertNotIn(2, tree)
        self.assertIn(5, tree)
        self.assertIn(10, tree)
        self.assertIn(15, tree)
        self.assertEqual(tree.root.left.key, 5)

    def test_delete_maximum(self):
        """Delete the maximum key and check the new maximum."""
        tree = RedBlackST()
        for k in [10, 5, 15, 20]:
            tree.put(k, str(k))
        tree.delete(20)
        self.assertEqual(tree.size(), 3)
        self.assertNotIn(20, tree)
        self.assertIn(5, tree)
        self.assertIn(10, tree)
        self.assertIn(15, tree)
        self.assertEqual(tree.root.right.key, 15)

    # Additional tests for better coverage

    def test_delete_root_with_two_children(self):
        """Delete the root when it has two children."""
        tree = RedBlackST()
        tree.put(10, "root")
        tree.put(5, "left")
        tree.put(15, "right")
        tree.delete(10)
        self.assertEqual(tree.size(), 2)
        self.assertNotIn(10, tree)
        self.assertIn(5, tree)
        self.assertIn(15, tree)
        self.assertIn(tree.root.key, [5, 15])

    def test_delete_root_with_one_child(self):
        """Delete the root when it has only one child."""
        tree = RedBlackST()
        tree.put(10, "root")
        tree.put(5, "left")
        tree.delete(10)
        self.assertEqual(tree.size(), 1)
        self.assertNotIn(10, tree)
        self.assertIn(5, tree)
        self.assertEqual(tree.root.key, 5)

    def test_delete_root_with_no_children(self):
        """Delete the root when it is the only node."""
        tree = RedBlackST()
        tree.put(10, "root")
        tree.delete(10)
        self.assertTrue(tree.is_empty())
        self.assertIsNone(tree.root)

    def test_delete_in_left_skewed_tree(self):
        """Delete from a left-skewed tree (degenerate case)."""
        tree = RedBlackST()
        for k in [10, 9, 8, 7, 6]:
            tree.put(k, str(k))
        tree.delete(8)
        self.assertEqual(tree.size(), 4)
        self.assertNotIn(8, tree)
        for k in [10, 9, 7, 6]:
            self.assertIn(k, tree)

    def test_delete_in_right_skewed_tree(self):
        """Delete from a right-skewed tree (degenerate case)."""
        tree = RedBlackST()
        for k in [1, 2, 3, 4, 5]:
            tree.put(k, str(k))
        tree.delete(4)
        self.assertEqual(tree.size(), 4)
        self.assertNotIn(4, tree)
        for k in [1, 2, 3, 5]:
            self.assertIn(k, tree)

    def test_delete_all_from_large_tree(self):
        """Delete all nodes from a larger tree one by one."""
        keys = [20, 10, 30, 5, 15, 25, 35]
        tree = RedBlackST()
        for k in keys:
            tree.put(k, str(k))
        for k in keys:
            tree.delete(k)
        self.assertTrue(tree.is_empty())
        self.assertEqual(tree.size(), 0)
        self.assertIsNone(tree.root)

    def test_delete_duplicate_deletes_only_once(self):
        """Deleting the same key twice should not raise and should only affect the tree once."""
        tree = RedBlackST()
        tree.put(10, "root")
        tree.put(5, "left")
        tree.delete(5)
        self.assertNotIn(5, tree)
        tree.delete(5)  # Should not raise
        self.assertNotIn(5, tree)
        self.assertEqual(tree.size(), 1)

    def test_delete_preserves_red_black_properties(self):
        """After deletion, the tree should still satisfy red-black properties."""
        # This test assumes RedBlackST has a method is_red_black_tree() for validation
        tree = RedBlackST()
        for k in [10, 5, 15, 2, 7, 12, 17]:
            tree.put(k, str(k))
        tree.delete(5)
        if hasattr(tree, "is_red_black_tree"):
            self.assertTrue(tree.is_red_black_tree())
        tree.delete(10)
        if hasattr(tree, "is_red_black_tree"):
            self.assertTrue(tree.is_red_black_tree())

    def test_delete_with_string_keys(self):
        """Delete nodes when keys are strings."""
        tree = RedBlackST()
        for k in ["d", "b", "f", "a", "c", "e", "g"]:
            tree.put(k, k.upper())
        tree.delete("b")
        self.assertNotIn("b", tree)
        self.assertIn("a", tree)
        self.assertIn("c", tree)
        self.assertEqual(tree.size(), 6)
        self.assertIsNotNone(tree.root, f"The root node is: {tree.root}")

    def test_delete_left_child(self):
        """Delete the left child from a three-node tree and verify postconditions."""
        tree = RedBlackST()
        tree.put(10, "root")
        tree.put(5, "left")
        tree.put(15, "right")
        tree.delete(5)
        self.assertEqual(tree.size(), 2)
        self.assertIn(10, tree)
        self.assertIn(15, tree)
        self.assertNotIn(5, tree)
        self.assertIn(tree.root.key, [10, 15])
        self.assertNotIn(5, tree)
        # self.assertEqual(set(tree.keys()), {10, 15})

    def test_delete_right_child(self):
        """Delete the right child from a three-node tree and verify postconditions."""
        tree = RedBlackST()
        tree.put(10, "root")
        tree.put(5, "left")
        tree.put(15, "right")
        tree.delete(15)
        self.assertEqual(tree.size(), 2)

    def test_delete_all_nodes_one_by_one(self):
        """Delete all nodes one by one and ensure the tree is empty at the end."""
        tree = RedBlackST()
        tree.put(10, "root")
        tree.put(5, "left")
        tree.put(15, "right")
        tree.delete(5)
        self.assertEqual(tree.size(), 2)
        tree.delete(15)
        self.assertEqual(tree.size(), 1)
        tree.delete(10)
        self.assertTrue(tree.is_empty())
        self.assertEqual(tree.size(), 0)
        self.assertIsNone(tree.root)

    def test_delete_non_existing_key_multiple_nodes(self):
        """Deleting a non-existing key from a multi-node RedBlackST should not change the tree."""
        tree = RedBlackST()
        tree.put(10, "root")
        tree.put(5, "left")
        tree.put(15, "right")
        before = [tree.root.key, tree.root.left.key if tree.root.left else None, tree.root.right.key if tree.root.right else None]
        tree.delete(99)  # 99 does not exist
        after = [tree.root.key, tree.root.left.key if tree.root.left else None, tree.root.right.key if tree.root.right else None]
        self.assertEqual(before, after)
        self.assertEqual(tree.size(), 3)

    def test_delete_from_larger_tree(self):
        """Delete a node from a larger tree and check structure and size."""
        tree = RedBlackST()
        for k in [20, 10, 30, 5, 15, 25, 35]:
            tree.put(k, str(k))
        tree.delete(10)
        self.assertEqual(tree.size(), 6)
        self.assertNotIn(10, tree)
        # Check all other keys are still present
        for k in [20, 5, 15, 25, 30, 35]:
            self.assertIn(k, tree)


if __name__ == '__main__':
    unittest.main()

