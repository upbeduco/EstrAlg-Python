from typing import Any, Optional
from src.c02_ESTBASICAS.LinkedList import Node # Import Node for internal use

class Queue:
    """
    Implements a First-In, First-Out (FIFO) queue using a linked list.
    Maintains head and tail pointers for O(1) enqueue and dequeue operations.
    """
    def __init__(self):
        """
        Initializes an empty Queue.
        """
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    def enqueue(self, item: Any):
        """
        Adds an item to the rear (end) of the queue.

        Args:
            item (Any): The item to be added.
        """
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self) -> Any:
        """
        Removes and returns the item from the front (head) of the queue.

        Returns:
            Any: The item removed from the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        data = self._head.data
        self._head = self._head.next
        if self._head is None: # If the last element was dequeued, tail should also be None
            self._tail = None
        self._size -= 1
        return data

    def peek(self) -> Any:
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            Any: The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._head.data

    def size(self) -> int:
        """
        Returns the number of items in the queue.

        Returns:
            int: The number of items.
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self._size == 0
