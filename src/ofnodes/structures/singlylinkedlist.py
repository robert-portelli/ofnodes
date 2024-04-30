from typing import Optional, Any

from ofnodes.nodes.singlynode import SinglyNode
from ofnodes.components.structures.descriptors import Head, Tail, Target
from ofnodes.components.structures.mixins import SearchMixin, RemoveMixin, InsertHeadMixin, InsertTailMixin, InsertAfterTargetMixin, InsertBeforeTargetMixin, PrintMixin

class SinglyLinkedList(SearchMixin, RemoveMixin, InsertHeadMixin, InsertTailMixin, InsertAfterTargetMixin, InsertBeforeTargetMixin, PrintMixin):
    """A class representing a singly linked list.

    This class provides functionality to create and manipulate a singly linked list
    data structure. Each node in the linked list contains a reference to the next
    node in the sequence.

    Attributes:
        _head (Optional[SinglyNode]): The head of the linked list.
        _tail (Optional[SinglyNode]): The tail of the linked list.
        _target (Optional[Any]): The target data or node instance.

    Examples:
        >>> linked_list = SinglyLinkedList()
        >>> linked_list
        SinglyLinkedList(head=None, tail=None, target=None)
    """

    __slots__ = ('_head', '_tail', '_target',)
    head = Head()
    tail = Tail()
    target = Target()
    def __init__(self, values=None) -> None:
        self._head: Optional[SinglyNode] = None
        self._tail: Optional[SinglyNode] = None
        self._target: Optional[Any|SinglyNode] = None
        if values:
            for value in values:
                self.tail = value

    def cycle_detection(self):

        if self.tail.next is not None:
            return True
        return False

    def __add__(self, other):
        self.tail = other  # tail attr will validate


    def __repr__(self) -> str:
        #return f"{type(self).__name__}(head={type(self.head).__name__}, tail={self.tail})"
        if not self._head:
            return "SinglyLinkedList()"
        node = self._head
        nodes = []
        while node:
            nodes.append(repr(node.data))
            node = node.next
        return f"{type(self).__name__}([" + ', '.join(nodes) + "])"

    def __str__(self) -> str:
        if not self._head:
            return "Empty Singly Linked List"
        node = self._head
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        return ' -> '.join(nodes)

    def __dir__(self) -> list[str]:
        # Get the list of attributes and methods from the parent classes
        parent_dir = set(super().__dir__())
        # Filter out private attributes and methods
        parent_dir = {attr for attr in parent_dir if attr not in {'_head', '_tail', '_target'}}
        # Return a sorted list of all attributes and methods
        return sorted(parent_dir)

    def bubble_sort(self, ascending=True):
        """Sorts the elements of the singly linked data structure in ascending order using the bubble sort algorithm.

        This method iteratively traverses the list and swaps adjacent elements if they are in the wrong order,
        until the list is sorted.

        Example:
            >>> sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            >>> sllist.bubble_sort()
            >>> sllist
            SinglyLinkedList([2, 4, 5, 6, 8])
            >>> str(sllist)
            '2 -> 4 -> 5 -> 6 -> 8'

        Note:
            - This method modifies the original linked list in place.
            - The comparison operation (`>`) is used for elements. For non-numeric data types,
            ensure that the `__gt__` method is defined appropriately for comparison.

        Time Complexity:
            - Best Case: O(n), when the list is already sorted.
            - Worst Case: O(n^2), when the list is in reverse order.
            - Average Case: O(n^2).
        """

        # Flag to indicate whether any swaps were made in the current pass
        swapped = True
        while swapped:
            swapped = False
            # Start from the head of the list
            current = self._head
            while current and current.next:  # Add condition to check current.next
                if current._data > current.next._data:
                    # Swap data of adjacent nodes
                    current._data, current.next._data = current.next._data, current._data
                    # Set swapped flag to True
                    swapped = True
                # Move to the next node
                current = current.next
        if not ascending:
            head_to_tail = self.head
            self.head = SinglyNode(self.tail.data)
            self.remove_tail()
            self.head + SinglyNode(self.tail.data)

if __name__ == "__main__":
    sllist = SinglyLinkedList([8, 2, 6, 4, 5])
    sllist.bubble_sort()
    head_to_tail = sllist.head
    sllist.head = SinglyNode(sllist.tail.data)
    sllist.remove_tail()
    sllist.head + SinglyNode(sllist.tail.data)
