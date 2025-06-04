from typing import Any, Optional

class Node:
    """
    Represents a node in a singly linked list.
    """
    def __init__(self, data: Any):
        """
        Initializes a new Node.

        Args:
            data (Any): The data to be stored in the node.
        """
        self.data = data
        self.next: Optional['Node'] = None

class LinkedList:
    """
    Implements a singly linked list with basic operations.
    Elements are added to the head of the list.
    """
    def __init__(self):
        """
        Initializes an empty LinkedList.
        """
        self._head: Optional[Node] = None
        self._size: int = 0

    def add(self, data: Any):
        """
        Adds a new element to the head of the list.

        Args:
            data (Any): The data to be added.
        """
        new_node = Node(data)
        new_node.next = self._head
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
            current = current.next
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

        if self._head.data == data:
            self._head = self._head.next
            self._size -= 1
            return True

        current = self._head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False

    def remove_head(self) -> Any:
        """
        Removes and returns the data from the head of the list.

        Returns:
            Any: The data from the removed head node.

        Raises:
            IndexError: If the list is empty.
        """
        if self.is_empty():
            raise IndexError("remove_head from empty list")
        
        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        return data

    def peek_head(self) -> Any:
        """
        Returns the data from the head of the list without removing it.

        Returns:
            Any: The data from the head node.

        Raises:
            IndexError: If the list is empty.
        """
        if self.is_empty():
            raise IndexError("peek_head from empty list")
        return self._head.data

    def __iter__(self):
        """
        Returns an iterator for the elements in the list, from head to tail.
        """
        current = self._head
        while current:
            yield current.data
            current = current.next
