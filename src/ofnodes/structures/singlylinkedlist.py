from typing import Optional, Any

from ofnodes.nodes.singlynode import SinglyNode
from ofnodes.components.structures.descriptors import Head, Tail, Target
from ofnodes.components.structures.mixins import SearchMixin, RemoveMixin, InsertHeadMixin, InsertTailMixin, InsertAfterTargetMixin, InsertBeforeTargetMixin, PrintMixin
from ofnodes.sorting.mixins import BubbleSortMixin, InsertionSortMixin, ReverseOrderMixin

class SinglyLinkedList(InsertionSortMixin, SearchMixin, RemoveMixin, InsertHeadMixin, InsertTailMixin, InsertAfterTargetMixin, InsertBeforeTargetMixin, PrintMixin, BubbleSortMixin, ReverseOrderMixin):
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
        excluded = {'_head', '_tail', '_target', 'reference_based_reverse_order', 'reference_based_bubble_sort','index_based_bubble_sort', 'index_based_reverse_order', 'index_based_insertion_sort'}
        parent_dir = {attr for attr in parent_dir if attr not in excluded}
        # Return a sorted list of all attributes and methods
        return sorted(parent_dir)

    def xinsertion_sort(self):
        if 'head' not in dir(self):
            raise TypeError("reference_based_bubble_sort can only be used on reference-based data structures like linked lists.")
        if not self.head or not self.head.next:  # it's a zero node or one node list
            raise ValueError("Cannot sort an empty or one node linked list.")
        prev = self._head
        current = self._head.next
        while current and prev:
            value = current.data
            j = self._head
            while j is not current and value > j.data:
                j = j.next
            if j is current:
                prev, current = current, current.next
                continue
            node = SinglyNode(value)
            node._next, j._next = j.next, node # insert node
            prev, current = current.next, current.next.next # remove "moved" node

    def xinsertion_sort(self):
        if 'head' not in dir(self):
            raise TypeError("insertion_sort can only be used on reference-based data structures like linked lists.")
        if not self.head or not self.head.next:  # it's a zero node or one node list
            raise ValueError("Cannot sort an empty or one node linked list.")
        prev = self.head
        current = self.head.next
        while current:  # traverse the unsorted portion
            j = self.head  # traverse the sorted portion
            while j is not current and j.next.data < current.data:  # `j` should not point to current
                j = j.next  # advance to next sorted node
            if j is not current:  # `j` should point to current
                setattr(prev, '_next', current.next)
                #prev._next = current.next  # point to the next unsorted node, bypass current node
                current = prev.next  # advance current to next unsorted node

                if j is self.head and j.data > current.data:  # the current node should point to old head
                    setattr(current, '_next', self.head)
                    #current._next = sllist.head  # point current at the head
                    self.head = current  # trigger setter to add new head
                else:  # it's some node between head and current that current should point to
                    setattr(current, '_next', self.head)
                    setattr(j, '_next', current)
                    #current._next = j.next
                    #j._next = current
            else: # `j` reached current implying `current` is sorted
                prev, current = current, current.next  # advance to next unsorted node

    def insertion_sort(self):
        if 'head' not in dir(self):
            raise TypeError("insertion_sort can only be used on reference-based data structures like linked lists.")
        if not self.head or not self.head.next:  # it's a zero node or one node list
            raise ValueError("Cannot sort an empty or one node linked list.")

        prev = self.head
        current = self.head._next
        while current:  # traverse the unsorted portion
            j = self._head  # traverse the sorted portion
            while j is not current and j._next.data < current.data:  # `j` should not point to current
                j = j._next  # advance to next sorted node
            if j is not current:  # then `j._next.data > current.data`` and `j` should point to current
                prev._next = current._next  # point to the next unsorted node, bypass current node, persist the reference to the next unsorted node

                if j is self._head and j.data > current.data:  # the current node should point to old head
                    current._next = self.head  # point current at the head
                    self.head = current  # trigger setter to add new head
                else:  # it's some node between head and current that current should point to
                    current._next = j._next
                    j._next = current
                current = prev._next  # advance current to next unsorted node
            else: # `j` reached current implying `current` is sorted
                prev, current = current, current._next  # advance to next unsorted node

    def bubble_sort(self, ascending=True):
        """Sorts the nodes of the singly linked data structure.

        Args:
            ascending (bool, optional): Specifies whether to sort the elements in ascending order (default) or descending order.

        Returns:
            None: This method modifies the original linked list in place.

        Examples:
            >>> sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            >>> sllist.bubble_sort()
            >>> sllist
            SinglyLinkedList([2, 4, 5, 6, 8])
            >>> sllist.bubble_sort(ascending=False)
            >>> sllist
            SinglyLinkedList([8, 6, 5, 4, 2])

        Notes:
            - The comparison operation (`>`) is used for elements. For non-numeric data types,
            ensure that the `__gt__` method is defined appropriately for comparison.
            - Time Complexity:
                - Best Case: O(n), when the list is already sorted.
                - Worst Case: O(n^2), when the list is in reverse order.
                - Average Case: O(n^2).
        """
        super().reference_based_bubble_sort(ascending)

    def reverse_order(self):
        """Reverses the order of elements in the singly linked data structure.

        Returns:
            None: This method modifies the original linked list in place.

        Examples:
            >>> sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            >>> sllist.reverse_order()
            >>> sllist
            SinglyLinkedList([5, 4, 6, 2, 8])

        Notes:
            - Time Complexity: O(n), where n is the number of elements in the linked list.
        """
        return super().reference_based_reverse_order()

if __name__ == "__main__":
    sllist = SinglyLinkedList([8, 2, 6, 4, 5])
    sllist.insertion_sort()