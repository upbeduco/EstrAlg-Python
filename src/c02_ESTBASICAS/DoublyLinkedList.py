from typing import Any, Optional

class DoubleNode:
    """
    Represents a node in a doubly linked list.
    """
    def __init__(self, data: Any):
        """
        Initializes a new DoubleNode.

        Args:
            data (Any): The data to be stored in the node.
        """
        self.data = data
        self._prev: Optional['DoubleNode'] = None
        self._next: Optional['DoubleNode'] = None

class DoublyLinkedList:
    """
    Implements a doubly linked list with basic operations.
    The 'add' method adds elements to the head of the list.
    """
    def __init__(self):
        """
        Initializes an empty DoublyLinkedList.
        """
        self._head: Optional[DoubleNode] = None
        self._tail: Optional[DoubleNode] = None
        self._size: int = 0

    def add(self, data: Any):
        """
        Adds a new element to the head of the list.

        Args:
            data (Any): The data to be added.
        """
        new_node = DoubleNode(data)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
            self._head._prev = new_node
            self._head = new_node
        self._size += 1

    def size(self) -> int:
        """
        Returns the number of elements in the list.

        Returns:
            int: The number of elements.
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Checks if the list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self._size == 0

    def contains(self, data: Any) -> bool:
        """
        Checks if the list contains a specific element.

        Args:
            data (Any): The data to search for.

        Returns:
            bool: True if the data is found, False otherwise.
        """
        current = self._head
        while current:
            if current.data == data:
                return True
            current = current._next
        return False

    def remove(self, data: Any) -> bool:
        """
        Removes the first occurrence of a specific element from the list.

        Args:
            data (Any): The data to be removed.

        Returns:
            bool: True if the data was removed, False otherwise.
        """
        if self.is_empty():
            return False

        current = self._head
        while current:
            if current.data == data:
                if current == self._head:
                    # Removing the head node
                    self._head = current._next
                    if self._head:
                        self._head._prev = None
                    else:
                        # List became empty
                        self._tail = None
                elif current == self._tail:
                    # Removing the tail node
                    self._tail = current._prev
                    if self._tail:
                        self._tail._next = None
                else:
                    # Removing a middle node
                    current._prev._next = current._next
                    current._next._prev = current._prev
                
                self._size -= 1
                return True
            current = current._next
        return False
