import unittest
from .red_black_st import RedBlackST, Node # Import Node to check color if needed

class TestRedBlackST(unittest.TestCase):
    def test_put_and_get(self):
        rb_st = RedBlackST()
        self.assertIsNone(rb_st.get('a'))
        
        # Test basic insertions
        rb_st.put('S', 1)
        rb_st.put('E', 2)
        rb_st.put('A', 3)
        rb_st.put('R', 4)
        rb_st.put('C', 5)
        rb_st.put('H', 6)
        rb_st.put('M', 7)
        rb_st.put('X', 8)
        rb_st.put('L', 9)
        rb_st.put('P', 10)

        self.assertEqual(rb_st.get('S'), 1)
        self.assertEqual(rb_st.get('E'), 2)
        self.assertEqual(rb_st.get('A'), 3)
        self.assertEqual(rb_st.get('R'), 4)
        self.assertEqual(rb_st.get('C'), 5)
        self.assertEqual(rb_st.get('H'), 6)
        self.assertEqual(rb_st.get('M'), 7)
        self.assertEqual(rb_st.get('X'), 8)
        self.assertEqual(rb_st.get('L'), 9)
        self.assertEqual(rb_st.get('P'), 10)
        self.assertIsNone(rb_st.get('Z')) # Non-existent key

        # Test updating a value
        rb_st.put('S', 100)
        self.assertEqual(rb_st.get('S'), 100)

        # Insert more elements to trigger balancing
        keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, char in enumerate(keys):
            rb_st.put(char, i)
        
        for i, char in enumerate(keys):
            self.assertEqual(rb_st.get(char), i)
        
        self.assertEqual(len(rb_st), len(keys)) # S, E, A etc were overwritten

    def test_len_and_size(self):
        rb_st = RedBlackST()
        self.assertEqual(len(rb_st), 0)
        self.assertEqual(rb_st.size(), 0)
        self.assertTrue(rb_st.is_empty())

        keys = ['S', 'E', 'A', 'R', 'C', 'H', 'M', 'X']
        for i, key in enumerate(keys):
            rb_st.put(key, i)
            self.assertEqual(len(rb_st), i + 1)
            self.assertEqual(rb_st.size(), i + 1)
            self.assertFalse(rb_st.is_empty())
        print(str(rb_st))        

        num_keys = len(keys)
        print(f"num_keys = {num_keys}")
        for i, key in enumerate(reversed(keys)): # Delete in reverse order of insertion
            rb_st.delete(key)
            print(len(rb_st), num_keys - 1 - i)
            self.assertEqual(len(rb_st), num_keys - 1 - i)
            self.assertEqual(rb_st.size(), num_keys - 1 - i)
        
        self.assertEqual(len(rb_st), 0)
        self.assertEqual(rb_st.size(), 0)
        self.assertTrue(rb_st.is_empty())

    def test_delete(self):
        rb_st = RedBlackST()
        # Using characters for easy ordering
        # SEARCHXMPL -> A C E H L M P R S X
        keys_values = {
            'S': 1, 'E': 2, 'A': 3, 'R': 4, 'C': 5, 
            'H': 6, 'M': 7, 'X': 8, 'L': 9, 'P': 10
        }
        
        # Insert initial set of keys
        for k, v in keys_values.items():
            rb_st.put(k, v)
        
        initial_size = len(keys_values)
        self.assertEqual(len(rb_st), initial_size)

        # Test deleting a non-existing key
        rb_st.delete('Z') # Should do nothing
        self.assertEqual(len(rb_st), initial_size)

        # Delete leaf node ('A' is a leaf in many configurations after these inserts)
        # To be sure, let's check its rank or what it would be after specific inserts.
        # For this specific set: A C E H L M P R S X
        # A is a leaf.
        rb_st.delete('A')
        self.assertIsNone(rb_st.get('A'))
        self.assertEqual(len(rb_st), initial_size - 1)
        initial_size -= 1

        # Delete node with one child (difficult to guarantee without inspecting tree)
        # The Red-Black property means "one child" scenarios are less direct than BST.
        # Deletion involves rotations and color flips.
        # We will rely on deleting various nodes and checking size and remaining keys.
        # Delete 'C'
        self.assertIsNotNone(rb_st.get('C'))
        rb_st.delete('C')
        self.assertIsNone(rb_st.get('C'))
        self.assertEqual(len(rb_st), initial_size - 1)
        initial_size -= 1

        # Delete node with two children (most nodes will be like this or transform to it)
        # Delete 'M' (likely has L and P or their successors)
        self.assertIsNotNone(rb_st.get('M'))
        rb_st.delete('M')
        self.assertIsNone(rb_st.get('M'))
        self.assertEqual(len(rb_st), initial_size - 1)
        initial_size -= 1
        # Check neighbors
        self.assertIsNotNone(rb_st.get('L'))
        self.assertIsNotNone(rb_st.get('P'))


        # Delete the root node (current root is likely 'H' or 'M' after some deletions)
        # Let's insert a known sequence to have a better idea of the root
        rb_st = RedBlackST()
        simple_keys = "SEARCH"
        for k in simple_keys: rb_st.put(k, ord(k))
        # Root after S,E,A,R,C,H (Sedgewick p437): H (black) with C(red), R(red) as children
        # Tree:        H(B)
        #            /    \
        #         C(R)    R(R)
        #        /  \    /  \
        #      A(B) E(B) S(B) <--- S should be > R, error in trace
        # Let's use Sedgewick's example order for Fig 3.3.16 (p.426) for insertion: A C E H L M P R S X
        rb_st = RedBlackST()
        ordered_keys = sorted(list(keys_values.keys())) # A C E H L M P R S X
        for k in ordered_keys:
            rb_st.put(k, keys_values[k])
        
        # After inserting A C E H L M P R S X, the root is H (Fig 3.3.16)
        self.assertEqual(rb_st.root.key, 'H')
        rb_st.delete('H') # Delete root
        self.assertIsNone(rb_st.get('H'))
        self.assertEqual(len(rb_st), len(ordered_keys) - 1)
        # New root should be black, and tree valid. (e.g. L could become root)
        if rb_st.root: # If tree not empty
             self.assertEqual(rb_st.root.color, Node.BLACK)
        
        initial_size = len(rb_st)

        # Delete 'S'
        rb_st.delete('S')
        self.assertIsNone(rb_st.get('S'))
        self.assertEqual(len(rb_st), initial_size - 1)
        initial_size -=1

        # Delete multiple elements to trigger various balancing scenarios
        keys_to_delete = ['E', 'X', 'L']
        for key in keys_to_delete:
            if rb_st.get(key): # if key still exists
                rb_st.delete(key)
                self.assertIsNone(rb_st.get(key))
                initial_size -= 1
                self.assertEqual(len(rb_st), initial_size)
                if rb_st.root:
                    self.assertEqual(rb_st.root.color, Node.BLACK)
        
        # Delete all remaining nodes
        # Since we don't have a keys() method yet for RedBlackST, we'll use the ones we know
        # Or, we can implement a temporary keys() or use the existing ones if they are still there.
        # The remaining keys from 'A C E H L M P R S X' after deleting H, S, E, X, L are: A, C, M, P, R
        remaining_keys_initial = ['A', 'C', 'M', 'P', 'R']
        
        current_keys_in_tree = []
        for k_check in ordered_keys: # Check which of the original keys are still there
            if rb_st.get(k_check) is not None:
                current_keys_in_tree.append(k_check)

        for k in current_keys_in_tree:
            rb_st.delete(k)
            self.assertIsNone(rb_st.get(k))
            if rb_st.root: # After deletion, if tree not empty, root must be black
                self.assertEqual(rb_st.root.color, Node.BLACK)

        self.assertEqual(len(rb_st), 0)
        self.assertTrue(rb_st.is_empty())

    def test_is_empty(self):
        rb_st = RedBlackST()
        self.assertTrue(rb_st.is_empty())
        rb_st.put('A', 1)
        self.assertFalse(rb_st.is_empty())
        rb_st.delete('A')
        self.assertTrue(rb_st.is_empty())
        
        # Test after multiple operations
        rb_st.put('B', 2)
        rb_st.put('C', 3)
        self.assertFalse(rb_st.is_empty())
        rb_st.delete('B')
        self.assertFalse(rb_st.is_empty())
        rb_st.delete('C')
        self.assertTrue(rb_st.is_empty())

    def test_min_and_max(self):
        rb_st = RedBlackST()
        keys = ['S', 'E', 'A', 'R', 'C', 'H', 'M', 'X']
        for i, key in enumerate(keys):
            rb_st.put(key, i)
        self.assertEqual(rb_st.min(), 'A')
        self.assertEqual(rb_st.max(), 'X')
        # After deleting min and max
        rb_st.delete('A')
        rb_st.delete('X')
        self.assertEqual(rb_st.min(), 'C')
        self.assertEqual(rb_st.max(), 'S')

    def test_contains(self):
        rb_st = RedBlackST()
        rb_st.put('A', 1)
        rb_st.put('B', 2)
        self.assertTrue(rb_st.contains('A'))
        self.assertTrue(rb_st.contains('B'))
        self.assertFalse(rb_st.contains('C'))
        rb_st.delete('A')
        self.assertFalse(rb_st.contains('A'))

    def test_keys_method(self):
        rb_st = RedBlackST()
        keys = ['S', 'E', 'A', 'R', 'C', 'H', 'M', 'X']
        for i, key in enumerate(keys):
            rb_st.put(key, i)
        if hasattr(rb_st, 'keys'):
            result_keys = list(rb_st.keys())
            self.assertEqual(sorted(result_keys), sorted(keys))
            # After deleting a key
            rb_st.delete('A')
            result_keys = list(rb_st.keys())
            self.assertNotIn('A', result_keys)

    def test_str_ascii_representation(self):
        rb_st = RedBlackST()
        for k in ['S', 'E', 'A', 'R', 'C', 'H', 'M']:
            rb_st.put(k, ord(k))
        tree_str = str(rb_st)
        for k in ['S', 'E', 'A', 'R', 'C', 'H', 'M']:
            self.assertRegex(tree_str, r"[\[\(]" + k + r"[\]\)]")
        # Check if root line contains a black or red node marker
        lines = [line for line in tree_str.splitlines() if line.strip()]
        self.assertTrue(('[' in lines[0]) or ('(' in lines[0]))  # Corrected assertion

    # Helper for checking Red-Black properties (optional, but good for deeper validation)
    # This would require access to the root node and a recursive helper.
    # For now, we assume the external behavior implies internal correctness.
    # def is_bst(self, node, min_key, max_key):
    #     if node is None: return True
    #     if (min_key is not None and node.key <= min_key) or \
    #        (max_key is not None and node.key >= max_key):
    #         return False
    #     return self.is_bst(node.left, min_key, node.key) and \
    #            self.is_bst(node.right, node.key, max_key)

    # def is_23(self, node): # Checks if no node has two red links connected to it
    #     if node is None: return True
    #     if rb_st.is_red(node.right): return False # Right link should be black
    #     if node != rb_st.root and rb_st.is_red(node) and rb_st.is_red(node.left): return False # No two reds in a row
    #     return self.is_23(node.left) and self.is_23(node.right)

    # def is_balanced(self, node): # Checks if all paths from root to null have same number of black links
    #     # This is harder to check without passing black height down
    #     pass

    # def test_red_black_properties_after_many_ops(self):
    #     rb_st = RedBlackST()
    #     # Insert many elements
    #     import random
    #     keys = list(range(100))
    #     random.shuffle(keys)
    #     for k in keys:
    #         rb_st.put(k, k)
        
    #     self.assertTrue(self.is_bst(rb_st.root, None, None))
    #     # self.assertTrue(self.is_23(rb_st.root)) 
    #     # Root must be black
    #     if rb_st.root:
    #         self.assertEqual(rb_st.root.color, Node.BLACK)

        # Delete many elements
        # random.shuffle(keys)
        # for i in range(50):
        #     rb_st.delete(keys[i])
        
        # self.assertTrue(self.is_bst(rb_st.root, None, None))
        # # self.assertTrue(self.is_23(rb_st.root))
        # if rb_st.root:
        #     self.assertEqual(rb_st.root.color, Node.BLACK)


if __name__ == '__main__':
    unittest.main()
