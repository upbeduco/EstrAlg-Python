# Implementation of the QuickFind Union-Find ADT

class QuickUnion(UnionFind):

    def is_connected(self, p:int, q:int) -> bool:
        """True is p is connected to q (possibly with some intermediaries in between)"""
        pass

    def find(self, p:int) -> int:
        """Finds the ID of the component of p"""
        pass

    def union(self, p:int,q:int):
        """Joint components p,q """
        pass

    def components(self) -> int:
        """Number of connected components (disjoint sets) in the structure"""
        pass

    