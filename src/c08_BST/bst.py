from typing import Any, Optional, List

class Node:
    """Node of a Binary Search Tree."""
    def __init__(self, key: Any, value: Any, count: int) -> None:
        self.key: Any = key
        self.value: Any = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.count: int = count
 
class BST:
    """Binary Search Tree implementation with key-value pairs."""

    def __init__(self) -> None:
        """Initialize an empty BST."""
        self.root: Node | None = None

    def size(self) -> int:
        """Return the total number of nodes in the BST."""
        return self._size(self.root)

    def _size(self, node: Node | None) -> int:
        """Return the number of nodes in the subtree rooted at node."""
        if node is None:
            return 0
        return node.count

    def put(self, key: Any, value: Any) -> None:
        """Insert key-value pair into the BST."""
        self.root = self._put(self.root, key, value)

    def _put(self, node: Node | None, key: Any, value: Any) -> Node:
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

    def get(self, key: Any) -> Optional[Any]:
        """Return value associated with key, or None if not found."""
        node = self._get(self.root, key)
        return node.value if node else None

    def _get(self, node: Node | None, key: Any) -> Node | None:
        """Helper for get: search for key in subtree rooted at node."""
        if node is None:
            return None
        
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node

    def __len__(self) -> int:
        """Return the number of nodes in the BST."""
        return self.size()

    def min(self) -> Optional[Any]:
        """Return the minimum key in the BST, or None if empty."""
        if self.root is None:
            return None
        return self._min(self.root).key

    def _min(self, node: Node) -> Node:
        """Helper for min: return node with minimum key in subtree."""
        if node.left is None:
            return node
        return self._min(node.left)

    def delete_min(self) -> None:
        """Remove the node with the minimum key."""
        if self.root is None:
            return
        self.root = self._delete_min(self.root)

    def _delete_min(self, node: Node) -> Node | None:
        """Helper for delete_min: remove min node in subtree."""
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete(self, key: Any) -> None:
        """Remove the node with the given key."""
        self.root = self._delete(self.root, key)

    def _delete(self, node: Node | None, key: Any) -> Node | None:
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

    def rank(self, key: Any) -> int:
        """Return the number of keys less than the given key."""
        return self._rank(key, self.root)

    def _rank(self, key: Any, node: Node | None) -> int:
        """Helper for rank: compute rank of key in subtree rooted at node."""
        if node is None:
            return 0
        
        if key < node.key:
            return self._rank(key, node.left)
        elif key > node.key:
            return 1 + self._size(node.left) + self._rank(key, node.right)
        else:
            return self._size(node.left)

    def select(self, k: int) -> Optional[Any]:
        """Return the key of rank k (0-based), or None if out of bounds."""
        node = self._select(self.root, k)
        return node.key if node else None

    def _select(self, node: Node | None, k: int) -> Node | None:
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

    def keys(self) -> List[Any]:
        """Return all keys in the BST in sorted order."""
        queue: List[Any] = []
        self._keys(self.root, queue)
        return queue

    def _keys(self, node: Node | None, queue: List[Any]) -> None:
        """Helper for keys: in-order traversal to collect keys."""
        if node is None:
            return
        self._keys(node.left, queue)
        queue.append(node.key)
        self._keys(node.right, queue)

    def pre_order_keys(self) -> List[Any]:
        """Return all keys in pre-order traversal."""
        queue: List[Any] = []
        self._pre_order_keys(self.root, queue)
        return queue

    def _pre_order_keys(self, node: Node | None, queue: List[Any]) -> None:
        """Helper for pre_order_keys: pre-order traversal to collect keys."""
        if node is None:
            return
        queue.append(node.key)
        self._pre_order_keys(node.left, queue)
        self._pre_order_keys(node.right, queue)

    def post_order_keys(self) -> List[Any]:
        """Return all keys in post-order traversal."""
        queue: List[Any] = []
        self._post_order_keys(self.root, queue)
        return queue

    def _post_order_keys(self, node: Node | None, queue: List[Any]) -> None:
        """Helper for post_order_keys: post-order traversal to collect keys."""
        if node is None:
            return
        self._post_order_keys(node.left, queue)
        self._post_order_keys(node.right, queue)
        queue.append(node.key)

    def max(self) -> Optional[Any]:
        """Return the maximum key in the BST, or None if empty."""
        if self.root is None:
            return None
        return self._max(self.root).key

    def _max(self, node: Node) -> Node:
        """Helper for max: return node with maximum key in subtree."""
        if node.right is None:
            return node
        return self._max(node.right)

    def __contains__(self, key: Any) -> bool:
        """Return True if key is in the BST, else False."""
        return self._get(self.root, key) is not None

    def __getitem__(self, key: Any) -> Any:
        """Return the value associated with key. Raise KeyError if not found."""
        node = self._get(self.root, key)
        if node is None:
            raise KeyError(f"Key {key} not found in BST.")
        return node.value

    def __str__(self) -> str:
        """Return an ASCII-art representation of the tree (root left, leaves right)."""
        def _display(node, prefix="", is_left=True):
            if node is None:
                return []
            lines = []
            if node.right is not None:
                new_prefix = prefix + ("│   " if is_left else "    ")
                lines += _display(node.right, new_prefix, False)
            lines.append(prefix + ("└── " if is_left else "┌── ") + str(node.key))
            if node.left is not None:
                new_prefix = prefix + ("    " if is_left else "│   ")
                lines += _display(node.left, new_prefix, True)
            return lines

        if self.root is None:
            return "<empty tree>"
        return "\n".join(_display(self.root, "", True))

if __name__ == "__main__":
    # Example usage: create a BST and print its ASCII-art representation
    bst = BST()
    # Insert some sample keys
    for key in [4, 2, 6, 1, 3, 5, 7]:
        bst.put(key, str(key))
    print("BST structure:")
    print(bst)
