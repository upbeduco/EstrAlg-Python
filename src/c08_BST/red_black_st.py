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
        self.root: Node | None = None

    def is_red(self, node: Node | None) -> bool:
        """Return True if node is red; None is considered black."""
        if node is None:
            return False
        return node.color == Node.RED

    def _size(self, node: Node | None) -> int:
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
        """Rotate node h left to fix right-leaning red link."""
        if h.right is None:
            raise ValueError("rotate_left called on a node with no right child")
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
        """Flip colors to split a temporary 4-node."""
        h.color = not h.color
        if h.left is not None:
            h.left.color = not h.left.color
        if h.right is not None:
            h.right.color = not h.right.color

    def put(self, key: Any, value: Any) -> None:
        # Insert key-value pair into the tree
        if value is None:
            self.delete(key)
            return
        self.root = self._put(self.root, key, value)
        self.root.color = Node.BLACK

    def _put(self, h: Node | None, key: Any, value: Any) -> Node:
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

    def _get(self, x: Node | None, key: Any) -> Optional[Any]:
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
        min_node = self._min(self.root)
        return min_node.key if min_node else None

    def _min(self, x: Node | None) -> Node | None:
        # Find node with minimum key
        if x is None:
            return None
        if x.left is None:
            return x
        return self._min(x.left)

    def max(self) -> Optional[Any]:
        # Return maximum key in the tree
        if self.is_empty():
            return None
        max_node = self._max(self.root)
        return max_node.key if max_node else None

    def _max(self, x: Node | None) -> Node | None:
        # Find node with maximum key
        if x is None:
            return None
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

    def _delete_min(self, h: Node | None) -> Node | None:
        # Recursive helper to delete minimum node
        if h is None:
            return None
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

    def _delete_max(self, h: Node) -> Node | None:
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

    def balance(self, h: Node) -> Node:
        # Restore red-black tree properties after modifications
        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)
        h.count = 1 + self._size(h.left) + self._size(h.right)
        # print(f"Balancing node with key: {h.key}, count updated to: {h.count}")  # Debug print
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

        # After deletion, if the tree is empty, ensure root is None
        if self.root is not None and self._size(self.root) == 0:
            self.root = None
        elif self.root is not None:
            self.root.color = Node.BLACK


    def _delete(self, h: Node | None, key: Any) -> Node | None:
        if h is None:
            return None

        if key < h.key:
            if not self.is_red(h.left) and h.left and not self.is_red(h.left.left):
                h = self.move_red_left(h)
            h.left = self._delete(h.left, key)
        else:
            if self.is_red(h.left):
                h = self.rotate_right(h)
            if key == h.key and h.left is None and h.right is None:
                return None  # No children case (leaf)
            if h.right and not self.is_red(h.right) and not self.is_red(h.right.left):
                h = self.move_red_right(h)
            if key == h.key:
                x = self._min(h.right)
                h.key = x.key
                h.value = x.value
                h.right = self._delete_min(h.right)
            else:
                h.right = self._delete(h.right, key)

        h = self.balance(h)
        h.count = 1 + self._size(h.left) + self._size(h.right)
        return h


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



"""


### **Deletion Process in a Red-Black Tree**
1. **Find the node to delete** (same as BST).
2. **Delete the node** (similar to BST, but with extra bookkeeping for RBT properties):
   - **Case 1: No children** → Simply remove the node.
   - **Case 2: One child** → Replace the node with its child.
   - **Case 3: Two children** → Replace the node with its in-order successor/predecessor, then recursively delete the successor/predecessor.
3. **Rebalance the tree** (the complex part for RBTs).

---

### **Rebalancing After Deletion**
When a node is deleted, it may violate RBT properties (e.g., if a black node was removed, causing a "black deficit"). The rebalancing process involves fixing these violations by examining the **sibling** of the deleted node and its **nephews**.

#### **Key Observations:**
- The deleted node is either:
  - A **red node** (no violation, since it doesn't affect black height).
  - A **black node** (violation: introduces a "double black" or "extra black" that must be resolved).
- The rebalancing cases depend on the **color of the sibling** and **its children**.

---

### **Rebalancing Cases (Fixing "Double Black")**
Let `x` be the "double black" node (the position where the deleted node was). We handle the following cases:

#### **Case 1: Sibling is Red**
- Rotate to make the sibling black.
- Recurse to resolve the new sibling (now black).

#### **Case 2: Sibling is Black and Both Nephews are Black**
- Recolor the sibling to **red**.
- Propagate the "double black" upward to the parent.

#### **Case 3: Sibling is Black, Near Nephew is Red, Far Nephew is Black**
- Rotate to make the near nephew the new sibling.
- Recurse into **Case 4**.

#### **Case 4: Sibling is Black, Far Nephew is Red**
- Rotate the sibling to balance the tree.
- Recolor to restore RBT properties.

---

### **Your Rebalancing Cases vs. Correct Ones**
Your description of "Left-Left," "Left-Right," etc., is **partially correct but incomplete**:
- The actual cases depend on **color**, not just structure.
- The standard RBT deletion fixes involve **4 main cases** (as above), not just rotations.

---

### **Final Notes**
- Your initial steps (finding the node, BST deletion) are correct.
- The rebalancing part needs refinement to properly handle the "double black" scenarios.
- The correct cases are based on **sibling and nephew colors**, not just their positions.

Would you like a more detailed breakdown of the rebalancing steps?

"""