
from typing import Optional, Any
from c02_ESTBASICAS.LinkedList import LinkedList

class SequentialSearch:
    """Sequential Search Symbol Table implemented with a linked list."""

    class Node:
        def __init__(self, key: Any, value: Any):
            self.key = key
            self.value = value

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, SequentialSearch.Node):
                return False
            return self.key == other.key

    def __init__(self):
        self._list = LinkedList()
        self._n: int = 0

    def size(self) -> int:
        """Return the number of key-value pairs."""
        return self._n

    def is_empty(self) -> bool:
        """Return True if the symbol table is empty."""
        return self._n == 0

    def get(self, key: Any) -> Optional[Any]:
        """Return the value associated with key, or None if not found."""
        for node in self._list:
            if node.key == key:
                return node.value
        return None

    def contains(self, key: Any) -> bool:
        """Return True if key is in the symbol table."""
        return self.get(key) is not None

    def put(self, key: Any, value: Any) -> None:
        """Insert key-value pair into the symbol table, or update value if key exists."""
        for node in self._list:
            if node.key == key:
                node.value = value
                return
        self._list.add(self.Node(key, value))
        self._n += 1

    def delete(self, key: Any) -> None:
        """Remove key and its value from the symbol table if present."""
        current = self._list._head
        prev = None
        while current is not None:
            if current.data.key == key:
                if prev is None:
                    self._list._head = current.next
                else:
                    prev.next = current.next
                self._n -= 1
                self._list._size -= 1
                return
            prev = current
            current = current.next

# TODO add unit tests of the data structure
