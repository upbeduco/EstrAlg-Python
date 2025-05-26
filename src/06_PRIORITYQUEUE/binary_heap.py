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

    def __str__(self) -> str:
        """Return a string representation of the heap."""
        return str(self._heap)

    def __len__(self) -> int:
        """Return the number of elements in the heap."""
        return len(self._heap)

    def __contains__(self, value: Any) -> bool:
        """Check if a value is in the heap."""
        return value in self._heap
    
    def __iter__(self) -> Iterator[Any]:
        """Return an iterator over the heap."""
        # TODO: should iterate in the priority order of the keys
        return iter(self._heap)
    
    def __next__(self) -> Any:
        """Return the next value in the heap."""
        return next(self._heap)
    
    def is_empty(self) -> bool:
        """Return True if the heap is empty, False otherwise."""
        return len(self._heap) == 0
    
    def size(self) -> int:
        """Return the number of elements in the heap."""
        return len(self._heap)
    
    def clear(self):
        """Remove all elements from the heap."""
        self._heap = []
    
