from c04_UF.UnionFind import UnionFind

class WeightedQuickUnion(UnionFind):
    """
    WeightedQuickUnion is an implementation of the Union-Find data structure.
    It improves upon QuickUnion by linking the root of the smaller tree to the
    root of the larger tree during the union operation. This helps to keep
    the trees relatively flat, ensuring that `find` operations are efficient
    (logarithmic time complexity).
    """

    def __init__(self, n: int):
        """
        Initializes the WeightedQuickUnion data structure with n elements.
        Each element is initially in its own component, its parent is itself,
        and the size of its component is 1.

        Args:
            n (int): The number of elements.
        """
        super().__init__()
        self._parent = list(range(n))  # Stores the parent of each element
        self._size = [1] * n  # Stores the size of the component for each root
        self._count = n  # Number of components

    def find(self, p: int) -> int:
        """
        Finds the root of the component containing element p.
        The root of a component is an element that is its own parent.
        This implementation includes path compression for optimization.

        Args:
            p (int): The element to find.

        Returns:
            int: The root of the component containing element p.

        Raises:
            ValueError: if p is out of bounds.
        """
        if not (0 <= p < len(self._parent)):
            raise ValueError(f"Element {p} is out of bounds.")
        
        # Navigate up the tree to find the root
        root = p
        while root != self._parent[root]:
            root = self._parent[root]
        
        # Path compression: make every node on the path point directly to the root
        while p != root:
            new_parent = self._parent[p]
            self._parent[p] = root
            p = new_parent
            
        return root

    def union(self, p: int, q: int):
        """
        Connects elements p and q by merging their components.
        The root of the smaller tree is linked to the root of the larger tree.

        Args:
            p (int): The first element.
            q (int): The second element.

        Raises:
            ValueError: if p or q are out of bounds.
        """
        if not (0 <= p < len(self._parent) and 0 <= q < len(self._parent)):
            raise ValueError(f"Elements {p} or {q} are out of bounds.")

        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return  # p and q are already in the same component

        # Link the smaller tree under the root of the larger tree
        if self._size[rootP] < self._size[rootQ]:
            self._parent[rootP] = rootQ
            self._size[rootQ] += self._size[rootP]
        else:
            self._parent[rootQ] = rootP
            self._size[rootP] += self._size[rootQ]
        
        self._count -= 1  # Decrement the number of components

    def components(self) -> int:
        """
        Returns the number of disjoint sets (components).

        Returns:
            int: The number of components.
        """
        return self._count

    def is_connected(self, p: int, q: int) -> bool:
        """
        Checks if elements p and q are in the same component.

        Args:
            p (int): The first element.
            q (int): The second element.

        Returns:
            bool: True if p and q are in the same component, False otherwise.
        
        Raises:
            ValueError: if p or q are out of bounds.
        """
        if not (0 <= p < len(self._parent) and 0 <= q < len(self._parent)):
            raise ValueError(f"Elements {p} or {q} are out of bounds.")
        return self.find(p) == self.find(q)
    
if __name__=="__main__":
    wqu = WeightedQuickUnion(5)
    wqu.union(1,2)
    wqu.union(0,4)
    print(wqu.components())
    print(wqu.is_connected(1,4))
    print(wqu.is_connected(2,1))