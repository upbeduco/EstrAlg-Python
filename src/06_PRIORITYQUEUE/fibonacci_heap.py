# An implementation of the Fibonacci Heap data structure
# API: insert, max, del_max, union, is_empty, size, clear, __str__

class FibonacciNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.degree = 0
        self.mark = False

    def __str__(self):
        return f"Node({self.key}, degree={self.degree})"

class FibonacciHeap:
    def __init__(self):
        self.max_node = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def clear(self):
        self.max_node = None
        self._size = 0

    def insert(self, key):
        node = FibonacciNode(key)
        self._merge_with_root_list(node)
        if not self.max_node or node.key > self.max_node.key:
            self.max_node = node
        self._size += 1

    def max(self):
        return self.max_node.key if self.max_node else None

    def del_max(self):
        z = self.max_node
        if not z:
            return None
        # Add children to root list
        if z.child:
            children = []
            child = z.child
            while True:
                children.append(child)
                child = child.right
                if child == z.child:
                    break
            for c in children:
                self._merge_with_root_list(c)
                c.parent = None
        # Remove z from root list
        self._remove_from_root_list(z)
        if z == z.right:
            self.max_node = None
        else:
            self.max_node = z.right
            self._consolidate()
        self._size -= 1
        return z.key

    def union(self, other):
        if not other or other.is_empty():
            return
        if self.is_empty():
            self.max_node = other.max_node
            self._size = other._size
            return
        # Merge root lists
        self._concatenate_root_lists(self.max_node, other.max_node)
        if other.max_node and (not self.max_node or other.max_node.key > self.max_node.key):
            self.max_node = other.max_node
        self._size += other._size

    def _merge_with_root_list(self, node):
        if not self.max_node:
            node.left = node.right = node
        else:
            node.left = self.max_node
            node.right = self.max_node.right
            self.max_node.right.left = node
            self.max_node.right = node

    def _remove_from_root_list(self, node):
        node.left.right = node.right
        node.right.left = node.left

    def _concatenate_root_lists(self, a, b):
        if not a or not b:
            return
        a_right = a.right
        b_left = b.left
        a.right = b
        b.left = a
        a_right.left = b_left
        b_left.right = a_right

    def _consolidate(self):
        import math
        max_degree = int(math.log2(self._size)) + 2
        A = [None] * max_degree
        # Gather root list nodes
        nodes = []
        x = self.max_node
        if x:
            while True:
                nodes.append(x)
                x = x.right
                if x == self.max_node:
                    break
        for w in nodes:
            x = w
            d = x.degree
            while A[d]:
                y = A[d]
                if x.key < y.key:
                    x, y = y, x
                self._link(y, x)
                A[d] = None
                d += 1
            A[d] = x
        # Rebuild root list and find new max
        self.max_node = None
        for node in A:
            if node:
                node.left = node.right = node
                self._merge_with_root_list(node)
                if not self.max_node or node.key > self.max_node.key:
                    self.max_node = node

    def _link(self, y, x):
        # Remove y from root list
        self._remove_from_root_list(y)
        # Make y a child of x
        y.left = y.right = y
        if not x.child:
            x.child = y
        else:
            y.right = x.child.right
            y.left = x.child
            x.child.right.left = y
            x.child.right = y
        y.parent = x
        x.degree += 1
        y.mark = False

    def __str__(self):
        if self.is_empty():
            return "FibonacciHeap()"
        result = []
        nodes = []
        x = self.max_node
        if x:
            while True:
                nodes.append(x)
                x = x.right
                if x == self.max_node:
                    break
        for node in nodes:
            result.append(self._str_tree(node))
        return "FibonacciHeap:\n" + "\n".join(result)

    def _str_tree(self, node, depth=0):
        result = "  " * depth + f"{node.key}\n"
        if node.child:
            children = []
            child = node.child
            while True:
                children.append(child)
                child = child.right
                if child == node.child:
                    break
            for c in children:
                result += self._str_tree(c, depth + 1)
        return result

    def __len__(self):
        """Implement len() for FibonacciHeap"""
        return self.size()
        
    def __contains__(self, key):
        """Implement 'in' operator for FibonacciHeap"""
        if self.is_empty():
            return False
        nodes = []
        x = self.max_node
        if x:
            while True:
                nodes.append(x)
                x = x.right
                if x == self.max_node:
                    break
        for node in nodes:
            if node.key == key:
                return True
        return False
    
    def __iter__(self):
        """Implement iteration over FibonacciHeap"""
        if self.is_empty():
            return iter([])
        nodes = []
        x = self.max_node
        if x:
            while True:
                nodes.append(x)
                x = x.right
                if x == self.max_node:
                    break
        return iter(nodes)
    