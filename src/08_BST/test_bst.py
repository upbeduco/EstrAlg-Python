# cd src
# python3 -m 08_BST.test_bst

import unittest
from .bst import BST

class TestBST(unittest.TestCase):
    def test_put_and_get(self):
        bst = BST()
        self.assertIsNone(bst.get('a'))
        bst.put('S', 1)
        bst.put('E', 2)
        bst.put('A', 3)
        bst.put('R', 4)
        bst.put('C', 5)
        bst.put('H', 6)
        bst.put('M', 7)
        bst.put('X', 8)

        self.assertEqual(bst.get('S'), 1)
        self.assertEqual(bst.get('E'), 2)
        self.assertEqual(bst.get('A'), 3)
        self.assertEqual(bst.get('R'), 4)
        self.assertEqual(bst.get('C'), 5)
        self.assertEqual(bst.get('H'), 6)
        self.assertEqual(bst.get('M'), 7)
        self.assertEqual(bst.get('X'), 8)
        self.assertIsNone(bst.get('Z'))

        bst.put('S', 10)
        self.assertEqual(bst.get('S'), 10)

    def test_len_and_size(self):
        bst = BST()
        self.assertEqual(len(bst), 0)
        self.assertEqual(bst.size(), 0)

        keys = ['S', 'E', 'A', 'R', 'C', 'H', 'M', 'X']
        for i, key in enumerate(keys):
            bst.put(key, i)
            self.assertEqual(len(bst), i + 1)
            self.assertEqual(bst.size(), i + 1)
        
        for i, key in enumerate(reversed(keys)):
            bst.delete(key)
            self.assertEqual(len(bst), len(keys) - 1 - i)
            self.assertEqual(bst.size(), len(keys) - 1 - i)
        
        self.assertEqual(len(bst), 0)
        self.assertEqual(bst.size(), 0)

    def test_delete(self):
        bst = BST()
        keys_values = {'S':1, 'E':2, 'A':3, 'R':4, 'C':5, 'H':6, 'M':7, 'X':8, 'L':9, 'P':10}
        for k,v in keys_values.items():
            bst.put(k,v)
        
        initial_size = len(keys_values)

        # Test deleting a non-existing key
        bst.delete('Z')
        self.assertEqual(len(bst), initial_size)

        # Delete leaf node ('A')
        bst.delete('A')
        self.assertIsNone(bst.get('A'))
        self.assertEqual(len(bst), initial_size - 1)

        # Delete node with one child ('C' which has 'H' or 'M' depending on insertion)
        # To ensure 'C' has one child, let's re-insert specific keys for this test
        bst = BST()
        bst.put('S',1); bst.put('E',2); bst.put('A',3); bst.put('C',4); bst.put('B',5) 
        # 'C' has left child 'B'
        self.assertEqual(len(bst), 5)
        bst.delete('C')
        self.assertIsNone(bst.get('C'))
        self.assertEqual(bst.get('B'), 5) # Ensure child is still there
        self.assertEqual(len(bst), 4)
        # Check root of subtree is now B
        # This requires inspecting the tree structure or relying on other functions
        # For now, we trust get and size

        bst = BST()
        bst.put('S',1); bst.put('E',2); bst.put('A',3); bst.put('C',4); bst.put('D',5) 
        # 'C' has right child 'D'
        self.assertEqual(len(bst), 5)
        bst.delete('C')
        self.assertIsNone(bst.get('C'))
        self.assertEqual(bst.get('D'), 5)
        self.assertEqual(len(bst), 4)


        # Delete node with two children ('E')
        bst = BST()
        keys_values = {'S':1, 'E':2, 'A':3, 'R':4, 'C':5, 'H':6, 'M':7, 'X':8, 'L':9, 'P':10}
        for k,v in keys_values.items():
            bst.put(k,v)
        
        self.assertEqual(bst.get('E'), 2)
        bst.delete('E') # 'E' has 'A' and 'R' as children (or their successors)
        self.assertIsNone(bst.get('E'))
        self.assertEqual(len(bst), len(keys_values) - 1)
        # Verify structure by checking other nodes
        self.assertEqual(bst.get('A'), 3)
        self.assertEqual(bst.get('R'), 4)
        self.assertEqual(bst.get('S'), 1) 

        # Delete root node ('S')
        bst.delete('S')
        self.assertIsNone(bst.get('S'))
        self.assertEqual(len(bst), len(keys_values) - 2)
        # The new root should be the successor of 'S' (e.g. 'X' or 'R' depending on what was min of right subtree)
        # This is hard to assert without knowing the exact successor chosen by min()
        # We can check that other nodes are still present
        self.assertEqual(bst.get('X'), 8)
        self.assertEqual(bst.get('M'), 7)

        # Delete all remaining nodes
        remaining_keys = list(bst.keys()) # Get current keys
        for k in remaining_keys:
            bst.delete(k)
        self.assertEqual(len(bst), 0)

    def test_rank_and_select(self):
        bst = BST()
        keys = "SEARCHXMPL" # Unsorted to test general case
        sorted_keys = sorted(list(set(keys))) # Unique sorted keys: A, C, E, H, L, M, P, R, S, X

        for i, key in enumerate(keys): # Insert them
            bst.put(key, i)
        
        self.assertEqual(len(bst), len(sorted_keys))

        # Test rank
        for i, key in enumerate(sorted_keys):
            self.assertEqual(bst.rank(key), i, f"Rank for {key} should be {i}")

        self.assertEqual(bst.rank('B'), sorted_keys.index('C')) # Rank of non-existent key
        self.assertEqual(bst.rank('D'), sorted_keys.index('E'))
        self.assertEqual(bst.rank('Y'), len(sorted_keys)) # Rank for key larger than all
        self.assertEqual(bst.rank('0'), 0) # Rank for key smaller than all

        # Test select
        for i, key in enumerate(sorted_keys):
            self.assertEqual(bst.select(i), key, f"Select for rank {i} should be {key}")
        
        self.assertIsNone(bst.select(len(sorted_keys))) # Rank out of bounds
        self.assertIsNone(bst.select(-1)) # Rank out of bounds


    def test_traversals(self):
        bst = BST()
        # Test with empty tree
        self.assertEqual(bst.keys(), [])
        self.assertEqual(bst.pre_order_keys(), [])
        self.assertEqual(bst.post_order_keys(), [])

        # Example from Sedgewick & Wayne, Algorithms 4th ed, page 399
        # For BST (not RedBlack)
        # put S E A R C H X M P L
        # In-order (keys): A C E H L M P R S X
        # Pre-order: S E A C H M L P R X
        # Post-order: C L P M H A R X E S (Note: Sedgewick's example might be slightly different based on specific Hibbard deletion or tie-breaking in put)
        # Let's use the standard Hibbard deletion for BST.
        # The post-order depends on the structure after deletions if any.
        # For a simple insertion sequence:
        # S
        # E S
        # A E S
        # A E R S (R > E, R < S)
        # A C E R S (C > A, C < E)
        # A C E H R S (H > E, H < R)
        # A C E H M R S (M > H, M < R)
        # A C E H L M P R S X (X > S) , (P > M, P < R), (L > H, L < M)
        # Final tree structure (simplified, may vary based on implementation details of _put and node counts)
        #            S
        #          /   \
        #         E     X
        #        / \
        #       A   R
        #        \  /
        #         C M
        #          / \
        #         H   P
        #          \
        #           L
        # (This is one possible BST structure, actual might differ. Pre/Post order depends on this)

        keys_to_insert = ['S', 'E', 'A', 'R', 'C', 'H', 'M', 'X', 'L', 'P']
        for key in keys_to_insert:
            bst.put(key, ord(key)) # Value doesn't matter for traversal order

        expected_in_order = sorted(list(set(keys_to_insert))) # A, C, E, H, L, M, P, R, S, X
        self.assertEqual(bst.keys(), expected_in_order)

        # Pre-order and Post-order are highly dependent on the exact structure
        # resulting from the insertion order.
        # Let's trace our BST's _put:
        # put(S) -> root = S
        # put(E) -> S.left = E
        # put(A) -> E.left = A
        # put(R) -> S.right = R (because E < S, R > S is false, R > E. S.right was None) -> Correction: R > E, so E.right = R (if E is current node)
        # Let's re-trace based on the code logic:
        # _put(S, val) -> root = Node(S)
        # _put(E, val) -> root.left = Node(E)
        # _put(A, val) -> root.left.left = Node(A)
        # _put(R, val) -> root.right = Node(R)  (S is root, R < S is false, R > S is false, R==S is false... error in trace)
        # Let's re-trace with the actual code:
        # S
        # E (S.left)
        # A (E.left)
        # R (S.right)
        # C (E.left.right, since C > A and C < E)
        # H (R.left, since H < R)
        # M (R.left.right, since M > H and M < R)
        # X (R.right, since X > R)
        # L (R.left.right.left, since L < M)
        # P (R.left.right.right, since P > M)
        #
        # Tree:
        #        S
        #      /   \
        #     E     R
        #    / \   / \
        #   A   C H   X
        #          \
        #           M
        #          / \
        #         L   P

        expected_pre_order = ['S', 'E', 'A', 'C', 'R', 'H', 'M', 'L', 'P', 'X']
        self.assertEqual(bst.pre_order_keys(), expected_pre_order)
        
        expected_post_order = ['C', 'A', 'L', 'P', 'M', 'H', 'X', 'R', 'E', 'S']
        self.assertEqual(bst.post_order_keys(), expected_post_order)

if __name__ == '__main__':
    unittest.main()
