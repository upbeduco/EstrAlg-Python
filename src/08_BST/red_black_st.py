class Node:
    RED = True
    BLACK = False

    def __init__(self, key, value, color, count):
        self.key = key
        self.value = value
        self.color = color
        self.count = count
        self.left = None
        self.right = None

class RedBlackST:
    def __init__(self):
        self.root = None

    def is_red(self, node):
        if node is None:
            return False  # None links are black
        return node.color == Node.RED

    def _size(self, node):
        if node is None:
            return 0
        return node.count
    
    def size(self):
        return self._size(self.root)

    def __len__(self):
        return self.size()

    def is_empty(self):
        return self.root is None

    def rotate_left(self, h):
        # assert (h is not None) and self.is_red(h.right)
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = Node.RED
        x.count = h.count
        h.count = 1 + self._size(h.left) + self._size(h.right)
        return x

    def rotate_right(self, h):
        # assert (h is not None) and self.is_red(h.left)
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = Node.RED
        x.count = h.count
        h.count = 1 + self._size(h.left) + self._size(h.right)
        return x

    def flip_colors(self, h):
        # assert (h is not None) and (h.left is not None) and (h.right is not None)
        # assert (not self.is_red(h) and self.is_red(h.left) and self.is_red(h.right)) or \
        #        (self.is_red(h) and not self.is_red(h.left) and not self.is_red(h.right))
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def balance(self, h):
        if self.is_red(h.right) and not self.is_red(h.left):
            h = self.rotate_left(h)
        if self.is_red(h.left) and self.is_red(h.left.left):
            h = self.rotate_right(h)
        if self.is_red(h.left) and self.is_red(h.right):
            self.flip_colors(h)
        
        h.count = 1 + self._size(h.left) + self._size(h.right)
        return h

    def put(self, key, value):
        if value is None:
            self.delete(key) # Or raise error, depends on desired behavior
            return
        self.root = self._put(self.root, key, value)
        self.root.color = Node.BLACK # Ensure root is always black

    def _put(self, h, key, value):
        if h is None:
            return Node(key, value, Node.RED, 1) # New nodes are red

        if key < h.key:
            h.left = self._put(h.left, key, value)
        elif key > h.key:
            h.right = self._put(h.right, key, value)
        else:
            h.value = value
        
        return self.balance(h)

    def get(self, key):
        if key is None:
            # Or raise error, depends on desired behavior
            return None 
        return self._get(self.root, key)

    def _get(self, x, key):
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.value
        return None # Key not found

    def min(self):
        if self.is_empty():
            # Or raise error
            return None
        return self._min(self.root).key

    def _min(self, x):
        if x.left is None:
            return x
        return self._min(x.left)

    def max(self):
        if self.is_empty():
            # Or raise error
            return None
        return self._max(self.root).key

    def _max(self, x):
        if x.right is None:
            return x
        return self._max(x.right)

    def delete_min(self):
        if self.is_empty():
            # Or raise error
            return

        # if both children of root are black, set root to red
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = Node.RED
        
        self.root = self._delete_min(self.root)
        if not self.is_empty():
            self.root.color = Node.BLACK

    def _delete_min(self, h):
        if h.left is None:
            return None # No more nodes to delete

        if not self.is_red(h.left) and not self.is_red(h.left.left):
            h = self.move_red_left(h)

        h.left = self._delete_min(h.left)
        return self.balance(h)

    def delete_max(self):
        if self.is_empty():
            # Or raise error
            return

        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = Node.RED

        self.root = self._delete_max(self.root)
        if not self.is_empty():
            self.root.color = Node.BLACK
            
    def _delete_max(self, h):
        if self.is_red(h.left): # Rotate right if left child is red
            h = self.rotate_right(h)
        
        if h.right is None:
            return None # No more nodes to delete

        if not self.is_red(h.right) and not self.is_red(h.right.left):
            h = self.move_red_right(h)

        h.right = self._delete_max(h.right)
        return self.balance(h)

    def move_red_left(self, h):
        # Assuming h is red and h.left and h.left.left are black,
        # make h.left or one of its children red.
        self.flip_colors(h)
        if self.is_red(h.right.left):
            h.right = self.rotate_right(h.right)
            h = self.rotate_left(h)
            self.flip_colors(h)
        return h

    def move_red_right(self, h):
        # Assuming h is red and h.right and h.right.left are black,
        # make h.right or one of its children red.
        self.flip_colors(h)
        if self.is_red(h.left.left):
            h = self.rotate_right(h)
            self.flip_colors(h)
        return h

    def delete(self, key):
        if key is None:
            # Or raise error
            return 
        if not self.get(key): # Key not in tree
            return

        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = Node.RED

        self.root = self._delete(self.root, key)
        if not self.is_empty():
            self.root.color = Node.BLACK
            
    def _delete(self, h, key):
        if key < h.key:
            if not self.is_red(h.left) and not self.is_red(h.left.left):
                h = self.move_red_left(h)
            h.left = self._delete(h.left, key)
        else:
            if self.is_red(h.left):
                h = self.rotate_right(h)
            if key == h.key and (h.right is None):
                return None # Found node, delete it
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
