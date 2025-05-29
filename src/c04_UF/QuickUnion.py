# Implementation of the QuickFind Union-Find ADT
from c04_UF.UnionFind import UnionFind

class QuickUnion(UnionFind):
    """
    QuickUnion is an implementation of the Union-Find data structure.
    It uses a lazy approach where `union` is fast (O(1) in the best case,
    O(n) in the worst case if not considering path compression), but `find`
    can be slow (O(n) in the worst case, proportional to the depth of the tree).
    """

    def __init__(self, n: int):
        """
        Initializes the QuickUnion data structure with n elements.
        Each element is initially in its own component, and its parent is itself.

        Args:
            n (int): The number of elements.
        """
        super().__init__()
        self._parent = list(range(n))  # Stores the parent of each element
        self._count = n  # Number of components

    def find(self, p: int) -> int:
        """
        Finds the root of the component containing element p.
        The root of a component is an element that is its own parent.

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
        while p != self._parent[p]:
            p = self._parent[p]
        return p

    def union(self, p: int, q: int):
        """
        Connects elements p and q by merging their components.
        The root of p's component becomes a child of the root of q's component.

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

        self._parent[rootP] = rootQ  # Set the root of p to be a child of the root of q
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
    qu = QuickUnion(5)
    qu.union(1,2)
    qu.union(0,4)
    print(qu.components())
    print(qu.is_connected(1,4))
    print(qu.is_connected(2,1))    