class Node:
    def __init__(self, key, value, count):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.count = count

class BST:
    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return node.count

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
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
        node = self._get(self.root, key)
        return node.value if node else None

    def _get(self, node, key):
        if node is None:
            return None
        
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node

    def __len__(self):
        return self.size()

    def min(self):
        if self.root is None:
            return None
        return self._min(self.root).key

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def delete_min(self):
        if self.root is None:
            return
        self.root = self._delete_min(self.root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
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
        return self._rank(key, self.root)

    def _rank(self, key, node):
        if node is None:
            return 0
        
        if key < node.key:
            return self._rank(key, node.left)
        elif key > node.key:
            return 1 + self._size(node.left) + self._rank(key, node.right)
        else:
            return self._size(node.left)

    def select(self, k):
        node = self._select(self.root, k)
        return node.key if node else None

    def _select(self, node, k):
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
        queue = []
        self._keys(self.root, queue)
        return queue

    def _keys(self, node, queue):
        if node is None:
            return
        self._keys(node.left, queue)
        queue.append(node.key)
        self._keys(node.right, queue)

    def pre_order_keys(self):
        queue = []
        self._pre_order_keys(self.root, queue)
        return queue

    def _pre_order_keys(self, node, queue):
        if node is None:
            return
        queue.append(node.key)
        self._pre_order_keys(node.left, queue)
        self._pre_order_keys(node.right, queue)

    def post_order_keys(self):
        queue = []
        self._post_order_keys(self.root, queue)
        return queue

    def _post_order_keys(self, node, queue):
        if node is None:
            return
        self._post_order_keys(node.left, queue)
        self._post_order_keys(node.right, queue)
        queue.append(node.key)
