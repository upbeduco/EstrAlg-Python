# An implementation of the Binomial Heap data structure
# API: insert, max, del_max, union, is_empty, size, clear, __str__

class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.degree = 0

    def __str__(self):
        return f"Node({self.key}, degree={self.degree})"

class BinomialHeap:
    def __init__(self):
        self.roots = []
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def clear(self):
        self.roots = []
        self._size = 0

    def insert(self, key):
        new_heap = BinomialHeap()
        new_heap.roots.append(BinomialNode(key))
        new_heap._size = 1
        self.union(new_heap)

    def max(self):
        if self.is_empty() or not self.roots:
            return None
        max_node = max(self.roots, key=lambda node: node.key)
        return max_node.key

    def del_max(self):
        if self.is_empty():
            return None
        # Find max root
        max_idx = 0
        for i in range(1, len(self.roots)):
            if self.roots[i].key > self.roots[max_idx].key:
                max_idx = i
        max_node = self.roots.pop(max_idx)
        # Create new heap from max_node's children
        new_heap = BinomialHeap()
        new_heap.roots = list(reversed(max_node.children))
        new_heap._size = sum(2 ** child.degree for child in new_heap.roots)
        self._size -= (1 + new_heap._size)
        self.union(new_heap)
        return max_node.key

    def union(self, other):
        # Merge root lists by degree
        self.roots = self._merge_roots(self.roots, other.roots)
        self._size += other._size
        if not self.roots:
            return
        new_roots = []
        i = 0
        while i < len(self.roots):
            curr = self.roots[i]
            # If last tree or next tree has different degree, just add
            if i + 1 == len(self.roots) or self.roots[i + 1].degree != curr.degree:
                new_roots.append(curr)
                i += 1
            else:
                next_node = self.roots[i + 1]
                # Merge curr and next_node
                if curr.key >= next_node.key:
                    curr.children.append(next_node)
                    curr.degree += 1
                    self.roots[i + 1] = curr
                else:
                    next_node.children.append(curr)
                    next_node.degree += 1
                i += 1  # Only advance by 1, since merged node may need to be merged again
        self.roots = new_roots

    def _merge_roots(self, roots1, roots2):
        # Merge two lists of roots sorted by degree
        result = []
        i = j = 0
        while i < len(roots1) and j < len(roots2):
            if roots1[i].degree < roots2[j].degree:
                result.append(roots1[i])
                i += 1
            else:
                result.append(roots2[j])
                j += 1
        result.extend(roots1[i:])
        result.extend(roots2[j:])
        return result

    def __str__(self):
        if self.is_empty():
            return "BinomialHeap()"
        result = []
        for root in self.roots:
            result.append(self._str_tree(root))
        return "BinomialHeap:\n" + "\n".join(result)

    def _str_tree(self, node, depth=0):
        result = "  " * depth + f"{node.key}\n"
        for child in node.children:
            result += self._str_tree(child, depth + 1)
        return result

