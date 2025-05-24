class Node:
    """Node of a Binary Search Tree."""
    def __init__(self, key, value, count):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.count = count
 
class BST:
    """Binary Search Tree implementation with key-value pairs."""

    def __init__(self):
        """Initialize an empty BST."""
        self.root = None

    def size(self):
        """Return the total number of nodes in the BST."""
        return self._size(self.root)

    def _size(self, node):
        """Return the number of nodes in the subtree rooted at node."""
        if node is None:
            return 0
        return node.count

    def put(self, key, value):
        """Insert key-value pair into the BST."""
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        """Helper for put: insert key-value in subtree rooted at node."""
        if node is None:
            return Node(key, value, 1)
        
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def get(self, key):
        """Return value associated with key, or None if not found."""
        node = self._get(self.root, key)
        return node.value if node else None

    def _get(self, node, key):
        """Helper for get: search for key in subtree rooted at node."""
        if node is None:
            return None
        
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node

    def __len__(self):
        """Return the number of nodes in the BST."""
        return self.size()

    def min(self):
        """Return the minimum key in the BST, or None if empty."""
        if self.root is None:
            return None
        return self._min(self.root).key

    def _min(self, node):
        """Helper for min: return node with minimum key in subtree."""
        if node.left is None:
            return node
        return self._min(node.left)

    def delete_min(self):
        """Remove the node with the minimum key."""
        if self.root is None:
            return
        self.root = self._delete_min(self.root)

    def _delete_min(self, node):
        """Helper for delete_min: remove min node in subtree."""
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete(self, key):
        """Remove the node with the given key."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """Helper for delete: remove key from subtree rooted at node."""
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            
            t = node
            node = self._min(t.right)
            node.right = self._delete_min(t.right)
            node.left = t.left
        
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def rank(self, key):
        """Return the number of keys less than the given key."""
        return self._rank(key, self.root)

    def _rank(self, key, node):
        """Helper for rank: compute rank of key in subtree rooted at node."""
        if node is None:
            return 0
        
        if key < node.key:
            return self._rank(key, node.left)
        elif key > node.key:
            return 1 + self._size(node.left) + self._rank(key, node.right)
        else:
            return self._size(node.left)

    def select(self, k):
        """Return the key of rank k (0-based), or None if out of bounds."""
        node = self._select(self.root, k)
        return node.key if node else None

    def _select(self, node, k):
        """Helper for select: find node of rank k in subtree."""
        if node is None:
            return None
        
        t = self._size(node.left)
        if t > k:
            return self._select(node.left, k)
        elif t < k:
            return self._select(node.right, k - t - 1)
        else:
            return node

    def keys(self):
        """Return all keys in the BST in sorted order."""
        queue = []
        self._keys(self.root, queue)
        return queue

    def _keys(self, node, queue):
        """Helper for keys: in-order traversal to collect keys."""
        if node is None:
            return
        self._keys(node.left, queue)
        queue.append(node.key)
        self._keys(node.right, queue)

    def pre_order_keys(self):
        """Return all keys in pre-order traversal."""
        queue = []
        self._pre_order_keys(self.root, queue)
        return queue

    def _pre_order_keys(self, node, queue):
        """Helper for pre_order_keys: pre-order traversal to collect keys."""
        if node is None:
            return
        queue.append(node.key)
        self._pre_order_keys(node.left, queue)
        self._pre_order_keys(node.right, queue)

    def post_order_keys(self):
        """Return all keys in post-order traversal."""
        queue = []
        self._post_order_keys(self.root, queue)
        return queue

    def _post_order_keys(self, node, queue):
        """Helper for post_order_keys: post-order traversal to collect keys."""
        if node is None:
            return
        self._post_order_keys(node.left, queue)
        self._post_order_keys(node.right, queue)
        queue.append(node.key)

    def max(self):
        """Return the maximum key in the BST, or None if empty."""
        if self.root is None:
            return None
        return self._max(self.root).key

    def _max(self, node):
        """Helper for max: return node with maximum key in subtree."""
        if node.right is None:
            return node
        return self._max(node.right)

    def __contains__(self, key):
        """Return True if key is in the BST, else False."""
        return self._get(self.root, key) is not None

    def __getitem__(self, key):
        """Return the value associated with key. Raise KeyError if not found."""
        node = self._get(self.root, key)
        if node is None:
            raise KeyError(f"Key {key} not found in BST.")
        return node.value
