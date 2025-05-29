# Implementation of the QuickFind Union-Find ADT
from c04_UF.UnionFind import UnionFind

class QuickFind(UnionFind):
    """
    QuickFind is an implementation of the Union-Find data structure.
    It uses an eager approach where `find` is fast (O(1) time complexity),
    but `union` is slow (O(n) time complexity).
    """

    def __init__(self, n: int):
        """
        Initializes the QuickFind data structure with n elements.
        Each element is initially in its own component.

        Args:
            n (int): The number of elements.
        """
        super().__init__()
        self._id = list(range(n))  # Stores the component id for each element
        self._count = n  # Number of components

    def find(self, p: int) -> int:
        """
        Finds the component identifier for element p.

        Args:
            p (int): The element to find.

        Returns:
            int: The component identifier for element p.
        
        Raises:
            ValueError: if p is out of bounds.
        """
        if not (0 <= p < len(self._id)):
            raise ValueError(f"Element {p} is out of bounds.")
        return self._id[p]

    def union(self, p: int, q: int):
        """
        Connects elements p and q by merging their components.

        Args:
            p (int): The first element.
            q (int): The second element.
        
        Raises:
            ValueError: if p or q are out of bounds.
        """
        if not (0 <= p < len(self._id) and 0 <= q < len(self._id)):
            raise ValueError(f"Elements {p} or {q} are out of bounds.")

        pid = self.find(p)
        qid = self.find(q)

        if pid == qid:
            return  # p and q are already in the same component

        # Change all elements in p's component to q's component
        for i in range(len(self._id)):
            if self._id[i] == pid:
                self._id[i] = qid
        
        self._count -= 1 # Decrement the number of components

    def components(self) -> int:
        """
        Returns the number of disjoint sets (components).

        Returns:
            int: The number of components.
        """
        return self._count

    def is_connected(self, p:int, q:int) -> bool:
        """True is p is connected to q (possibly with some intermediaries in between)"""
        if not (0 <= p < len(self._id) and 0 <= q < len(self._id)):
            raise ValueError(f"Elements {p} or {q} are out of bounds.")
        return self.find(p) == self.find(q)


if __name__=="__main__":
    qf = QuickFind(5)
    qf.union(1,2)
    qf.union(0,4)
    print(qf.components())
    print(qf.is_connected(1,4))
    print(qf.is_connected(2,1))