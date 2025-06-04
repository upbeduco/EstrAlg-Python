from typing import Any
from src.c02_ESTBASICAS.LinkedList import LinkedList

class Stack:
    """
    Implements a Last-In, First-Out (LIFO) stack using a linked list.
    """
    def __init__(self):
        """
        Initializes an empty Stack.
        """
        self._list = LinkedList()

    def push(self, item: Any):
        """
        Adds an item to the top of the stack.

        Args:
            item (Any): The item to be added.
        """
        self._list.add(item) # LinkedList.add adds to head, which is efficient for stack push

    def pop(self) -> Any:
        """
        Removes and returns the item from the top of the stack.

        Returns:
            Any: The item removed from the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        return self._list.remove_head() # LinkedList.remove_head removes from head, efficient for stack pop

    def peek(self) -> Any:
        """
        Returns the item at the top of the stack without removing it.

        Returns:
            Any: The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        return self._list.peek_head()

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self._list.is_empty()

    def size(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items.
        """
        return self._list.size()

    def __iter__(self):
        """
        Returns an iterator for the elements in the stack, from top to bottom (LIFO order).
        """
        return iter(self._list) # Delegate to the underlying LinkedList's iterator
