from abc import ABC, abstractmethod

class UnionFind(ABC):

    def is_connected(self, p:int, q:int) -> bool:
        """True is p is connected to q (possibly with some intermediaries in between)"""
        return self.find(p)==self.find(q)

    @abstractmethod
    def find(self, p:int) -> int:
        """Finds the ID of the component of p"""
        pass

    @abstractmethod
    def union(self, p:int,q:int):
        """Joint components p,q """
        pass

    @abstractmethod
    def components(self) -> int:
        """Returns the number of connected components (partitions) in the data structure"""
        pass