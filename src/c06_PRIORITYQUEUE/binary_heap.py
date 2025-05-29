# An implementation of the Binary Heap data structure

from typing import Any, Iterator


class BinaryHeap:

    def __init__(self):
        """Initialize an empty binary heap."""
        self._heap = []

    def max(self) -> Any: 
        """Return the maximum value in the heap."""
        if not self._heap:
            return None
        return self._heap[0]

    def del_max(self) -> Any:
        """Delete and return the maximum value in the heap."""
        if not self._heap:
            return None
        max = self._heap[0]
        self._heap[0] = self._heap[-1]
        self._heap.pop()
        if self._heap:  # Only sink if heap is not empty
            self._sink(0)
        return max

    def insert(self, value: Any):
        """Insert a value into the heap."""
        self._heap.append(value)
        self._swim(len(self._heap) - 1)

    def _swim(self, index: int):
        """Helper method to swim up the heap."""
        parent_index = (index - 1) // 2
        while index > 0 and self._heap[index] > self._heap[parent_index]:
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _sink(self, index: int):
        """Helper method to sink down the heap."""
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index
            
            if left_child_index < len(self._heap) and self._heap[left_child_index] > self._heap[largest]:
                largest = left_child_index
            if right_child_index < len(self._heap) and self._heap[right_child_index] > self._heap[largest]:
                largest = right_child_index
                
            if largest == index:
                break
                
            self._heap[index], self._heap[largest] = self._heap[largest], self._heap[index]
            index = largest

    def __str__(self):
        if self.size() == 0:
            return "BinaryHeap()"
        return f"BinaryHeap({list(self)})"

    def __len__(self) -> int:
        """Return the number of elements in the heap."""
        return len(self._heap)

    def __contains__(self, value: Any) -> bool:
        """Check if a value is in the heap."""
        return value in self._heap
    
    def __iter__(self) -> Iterator[Any]:
        """Return an iterator over the heap."""
        self._iter_index = 0
        return self

    def __next__(self) -> Any:
        """Return the next value in the heap."""
        if self._iter_index >= len(self._heap):
            raise StopIteration
        value = self._heap[self._iter_index]
        self._iter_index += 1
        return value
    
    def is_empty(self) -> bool:
        """Return True if the heap is empty, False otherwise."""
        return len(self._heap) == 0
    
    def size(self) -> int:
        """Return the number of elements in the heap."""
        return len(self._heap)
    
    def clear(self):
        """Remove all elements from the heap."""
        self._heap = []
    
    def union(self, other: 'BinaryHeap'):
        """Union with another binary heap."""
        for value in other:
            self.insert(value)

        