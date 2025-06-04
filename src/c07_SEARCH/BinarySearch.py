
from typing import List, Optional, Any

class BinarySearch:
    """Binary Search Symbol Table implemented with sorted arrays."""

    def __init__(self):
        self._keys: List[Any] = []
        self._values: List[Any] = []

    def size(self) -> int:
        """Return the number of key-value pairs."""
        return len(self._keys)

    def is_empty(self) -> bool:
        """Return True if the symbol table is empty."""
        return self.size() == 0

    def rank(self, key: Any) -> int:
        """Return the number of keys less than key."""
        lo, hi = 0, self.size() - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self._keys[mid] < key:
                lo = mid + 1
            elif self._keys[mid] > key:
                hi = mid - 1
            else:
                return mid
        return lo

    def get(self, key: Any) -> Optional[Any]:
        """Return the value associated with key, or None if not found."""
        if self.is_empty():
            return None
        i = self.rank(key)
        if i < self.size() and self._keys[i] == key:
            return self._values[i]
        return None

    def contains(self, key: Any) -> bool:
        """Return True if key is in the symbol table."""
        return self.get(key) is not None

    def put(self, key: Any, value: Any) -> None:
        """Insert key-value pair into the symbol table, or update value if key exists."""
        i = self.rank(key)
        if i < self.size() and self._keys[i] == key:
            self._values[i] = value
            return
        self._keys.insert(i, key)
        self._values.insert(i, value)

    def delete(self, key: Any) -> None:
        """Remove key and its value from the symbol table if present."""
        if self.is_empty():
            return
        i = self.rank(key)
        if i < self.size() and self._keys[i] == key:
            self._keys.pop(i)
            self._values.pop(i)

    def min(self) -> Optional[Any]:
        """Return the smallest key."""
        if self.is_empty():
            return None
        return self._keys[0]

    def max(self) -> Optional[Any]:
        """Return the largest key."""
        if self.is_empty():
            return None
        return self._keys[-1]

    def select(self, k: int) -> Optional[Any]:
        """Return the key of rank k."""
        if k < 0 or k >= self.size():
            return None
        return self._keys[k]

# TODO add unit tests of the data structure
