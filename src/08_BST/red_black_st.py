from typing import Optional, Any

class Node:
    RED = True
    BLACK = False

    def __init__(self, key: Any, value: Any, color: bool, count: int):
        self.key: Any = key
        self.value: Any = value
        self.color: bool = color  # Node color: RED or BLACK
        self.count: int = count  # Number of nodes in subtree
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

class RedBlackST:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def is_red(self, node: Optional[Node]) -> bool:
        """Return True if node is red; None is considered black."""
        if node is None:
            return False
        return node.color == Node.RED

    def _size(self, node: Optional[Node]) -> int:
        # Return size of subtree rooted at node
        if node is None:
            return 0
        return node.count
    
    def size(self) -> int:
        # Return total number of nodes in the tree
        return self._size(self.root)

    def __len__(self) -> int:
        # Enable len() support
        return self.size()

    def is_empty(self) -> bool:
        # Check if tree is empty
        return self.root is None

    def rotate_left(self, h: Node) -> Node:
        # Rotate node h left to fix right-leaning red link
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = Node.RED
        x.count = h.count
        h.count = 1 + self._size(h.left) + self._size(h.right)
        return x

    def rotate_right(self, h: Node) -> Node:
        # Rotate node h right to fix two consecutive left-leaning red links
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = Node.RED
        x.count = h.count
        h.count = 1 + self._size(h.left) + self._size(h.right)
        return x

    def flip_colors(self, h: Node) -> None:
        # Flip colors to split a temporary 4-node
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def balance(self, h: Node) -> Node:
        # Restore red-black tree properties after modifications
        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)
        h.count = 1 + self._size(h.left) + self._size(h.right)
        return h

    def put(self, key: Any, value: Any) -> None:
        # Insert key-value pair into the tree
        if value is None:
            self.delete(key)
            return
        self.root = self._put(self.root, key, value)
        self.root.color = Node.BLACK

    def _put(self, h: Optional[Node], key: Any, value: Any) -> Node:
        # Recursive helper for put
        if h is None:
            return Node(key, value, Node.RED, 1)
        if key < h.key:
            h.left = self._put(h.left, key, value)
        elif key > h.key:
            h.right = self._put(h.right, key, value)
        else:
            h.value = value
        return self.balance(h)

    def get(self, key: Any) -> Optional[Any]:
        # Retrieve value for key, or None if not found
        if key is None:
            return None
        return self._get(self.root, key)

    def _get(self, x: Optional[Node], key: Any) -> Optional[Any]:
        # Iterative search for key
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.value
        return None

    def min(self) -> Optional[Any]:
        # Return minimum key in the tree
        if self.is_empty():
            return None
        return self._min(self.root).key

    def _min(self, x: Node) -> Node:
        # Find node with minimum key
        if x.left is None:
            return x
        return self._min(x.left)

    def max(self) -> Optional[Any]:
        # Return maximum key in the tree
        if self.is_empty():
            return None
        return self._max(self.root).key

    def _max(self, x: Node) -> Node:
        # Find node with maximum key
        if x.right is None:
            return x
        return self._max(x.right)

    def delete_min(self) -> None:
        # Remove node with minimum key
        if self.is_empty():
            return
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = Node.RED
        self.root = self._delete_min(self.root)
        if not self.is_empty():
            self.root.color = Node.BLACK

    def _delete_min(self, h: Node) -> Optional[Node]:
        # Recursive helper to delete minimum node
        if h.left is None:
            return None
        if not self.is_red(h.left) and not self.is_red(h.left.left):
            h = self.move_red_left(h)
        h.left = self._delete_min(h.left)
        return self.balance(h)

    def delete_max(self) -> None:
        # Remove node with maximum key
        if self.is_empty():
            return
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = Node.RED
        self.root = self._delete_max(self.root)
        if not self.is_empty():
            self.root.color = Node.BLACK

    def _delete_max(self, h: Node) -> Optional[Node]:
        # Recursive helper to delete maximum node
        if self.is_red(h.left):
            h = self.rotate_right(h)
        if h.right is None:
            return None
        if not self.is_red(h.right) and not self.is_red(h.right.left):
            h = self.move_red_right(h)
        h.right = self._delete_max(h.right)
        return self.balance(h)

    def move_red_left(self, h: Node) -> Node:
        # Ensure left child or one of its children is red
        self.flip_colors(h)
        if self.is_red(h.right.left):
            h.right = self.rotate_right(h.right)
            h = self.rotate_left(h)
            self.flip_colors(h)
        return h

    def move_red_right(self, h: Node) -> Node:
        # Ensure right child or one of its children is red
        self.flip_colors(h)
        if self.is_red(h.left.left):
            h = self.rotate_right(h)
            self.flip_colors(h)
        return h

    def delete(self, key: Any) -> None:
        # Remove node with given key
        if key is None:
            return 
        if not self.get(key):
            return
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = Node.RED
        self.root = self._delete(self.root, key)
        if self.root is not None:
            self.root.color = Node.BLACK
        # Fix: If the tree is empty after deletion, ensure root is None
        if self.size() == 0:
            self.root = None

    def _delete(self, h: Node, key: Any) -> Optional[Node]:
        if key < h.key:
            if not self.is_red(h.left) and not self.is_red(h.left.left):
                h = self.move_red_left(h)
            h.left = self._delete(h.left, key)
        else:
            if self.is_red(h.left):
                h = self.rotate_right(h)
            # Fix: Return left child if right is None
            if key == h.key and h.right is None:
                return h.left  # Corrected line
            if not self.is_red(h.right) and not self.is_red(h.right.left):
                h = self.move_red_right(h)
            if key == h.key:
                x = self._min(h.right)
                h.key = x.key
                h.value = x.value
                h.right = self._delete_min(h.right)
            else:
                h.right = self._delete(h.right, key)
        return self.balance(h)

    def __contains__(self, key: Any) -> bool:
        # Return True if key is in the tree, else False
        return self.get(key) is not None

    def __getitem__(self, key: Any) -> Any:
        # Return value associated with key, raise KeyError if not found
        value = self.get(key)
        if value is None:
            raise KeyError(f"Key {key} not found in RedBlackST.")
        return value

    def contains(self, key: Any) -> bool:
        # Alias for __contains__ to match test expectations
        return self.__contains__(key)

    def __str__(self) -> str:
        # ASCII-art representation: root to the left, leaves to the right, with lines and color
        def _display(node, prefix="", is_left=True):
            if node is None:
                return []
            lines = []
            if node.right is not None:
                new_prefix = prefix + ("│   " if is_left else "    ")
                lines += _display(node.right, new_prefix, False)
            # Use (key) for RED, [key] for BLACK
            label = f"({node.key})" if node.color == Node.RED else f"[{node.key}]"
            lines.append(prefix + ("└── " if is_left else "┌── ") + label)
            if node.left is not None:
                new_prefix = prefix + ("    " if is_left else "│   ")
                lines += _display(node.left, new_prefix, True)
            return lines

        if self.root is None:
            return "<empty tree>"
        return "\n".join(_display(self.root, "", True))

if __name__ == "__main__":
    # Example usage: create a RedBlackST and print its ASCII-art representation
    rbst = RedBlackST()
    # Insert some sample keys, with some keys inserted in an order that will create red links
    # The order below will likely create red nodes at 2, 3, 5, depending on balancing
    for key in [4, 2, 6, 1, 3, 5, 7, 0]:
        rbst.put(key, str(key))
    print("RedBlackST structure:")
    print(rbst)
