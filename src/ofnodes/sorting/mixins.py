from ofnodes.nodes.singlynode import SinglyNode

class BubbleSortMixin:
    """Mixin class providing bubble sort functionality for linked node structures."""
    def bubble_sort(self, ascending=True):
        """Sorts the elements of the singly linked data structure.

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
        if not self.head or not self.head.next:  # it's a zero node or one node list
            raise ValueError("Cannot sort an empty linked list.")
        # Flag to indicate whether any swaps were made in the current pass
        swapped = True
        while swapped:
            swapped = False
            # Start from the head of the list
            # Complete ascending sort
            current = self._head
            while current and current.next:  # Add condition to check current.next
                if current._data > current.next._data:
                    # Swap data of adjacent nodes
                    current._data, current.next._data = current.next._data, current._data
                    # Set swapped flag to True
                    swapped = True
                # Move to the next node
                current = current.next
        if not ascending:  # it's descending
            self.reverse_order()

class ReverseOrderMixin:
    """Mixin class supporting node order reversal for linked node structures."""
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
        if not self.head or not self.head.next:  # it's a zero node or one node list
            raise ValueError("Cannot reverse an empty linked list.")
        ## it's more than one node list
        # set the head
        self.head = SinglyNode(self.tail.data)  # trigger the setter
        self.remove_tail()  # remove the node you moved data from
        # complete node order reversal
        current = self._head
        while current is not self.tail:  # or while head_to_tail.next is not None
            node = SinglyNode(self._tail.data)
            node._next, current._next = current._next, node
            self.remove_tail()
            current = current.next