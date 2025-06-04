
from typing import Optional, Any
from c02_ESTBASICAS.LinkedList import LinkedList

class SequentialSearch:
    """Sequential Search Symbol Table implemented with a linked list using (key,value) tuples."""

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
        for (k, v) in self._list:
            if k == key:
                return v
        return None

    def contains(self, key: Any) -> bool:
        """Return True if key is in the symbol table."""
        return self.get(key) is not None

    def put(self, key: Any, value: Any) -> None:
        """Insert key-value pair into the symbol table, or update value if key exists."""
        current = self._list._head
        while current is not None:
            k, _ = current.data
            if k == key:
                current.data = (key, value)
                return
            current = current.next
        self._list.add((key, value))
        self._n += 1

    def delete(self, key: Any) -> None:
        """Remove key and its value from the symbol table if present."""
        current = self._list._head
        prev = None
        while current is not None:
            k, _ = current.data
            if k == key:
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
