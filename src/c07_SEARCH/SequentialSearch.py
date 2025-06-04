
from typing import Optional, Any

class SequentialSearch:
    """Sequential Search Symbol Table implemented with a linked list."""

    class Node:
        def __init__(self, key: Any, value: Any, next: Optional['SequentialSearch.Node'] = None):
            self.key = key
            self.value = value
            self.next = next

    def __init__(self):
        self._head: Optional[SequentialSearch.Node] = None
        self._n: int = 0

    def size(self) -> int:
        """Return the number of key-value pairs."""
        return self._n

    def is_empty(self) -> bool:
        """Return True if the symbol table is empty."""
        return self._n == 0

    def get(self, key: Any) -> Optional[Any]:
        """Return the value associated with key, or None if not found."""
        current = self._head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def contains(self, key: Any) -> bool:
        """Return True if key is in the symbol table."""
        return self.get(key) is not None

    def put(self, key: Any, value: Any) -> None:
        """Insert key-value pair into the symbol table, or update value if key exists."""
        current = self._head
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        self._head = self.Node(key, value, self._head)
        self._n += 1

    def delete(self, key: Any) -> None:
        """Remove key and its value from the symbol table if present."""
        prev = None
        current = self._head
        while current is not None:
            if current.key == key:
                if prev is None:
                    self._head = current.next
                else:
                    prev.next = current.next
                self._n -= 1
                return
            prev = current
            current = current.next

# TODO add unit tests of the data structure
