from ofnodes.nodes.singlynode import SinglyNode

class BubbleSortMixin:
    """Mixin class providing bubble sort functionality for data structures."""
    def reference_based_bubble_sort(self, ascending=True):
        """Sorts the nodes of the singly linked data structure.

        Args:
            ascending (bool, optional): Specifies whether to sort the elements in ascending order (default) or descending order.

        Returns:
            None: This method modifies the original linked list in place.

        Examples:
            >>> sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            >>> sllist.reference_based_bubble_sort()
            >>> sllist
            SinglyLinkedList([2, 4, 5, 6, 8])
            >>> sllist.reference_based_bubble_sort(ascending=False)
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

        swapped = True
        while swapped:
            swapped = False
            # Complete ascending sort
            current = self._head
            while current.next:
                if current._data > current.next._data:
                    current._data, current.next._data = current.next._data, current._data
                    swapped = True
                current = current.next
        if not ascending:  # it's descending
            self.reverse_order()

    def index_based_bubble_sort(self, ascending= True):
        """
        Examples:
            >>> raarray = RandomAccessArray(5)
            >>> [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            [None, None, None, None, None]
            >>> raarray.index_based_bubble_sort()
            >>> raarray
            RandomAccessArray([2, 4, 5, 6, 8])
            >>> raarray.index_based_bubble_sort(ascending=False)
            >>> raarray
            RandomAccessArray([8, 6, 5, 4, 2])
        """
        if '__getitem__' not in dir(self):
            raise TypeError("index_based_bubble_sort can only be used on data structures that support index-based access.")
        n = len(self)
        for i in range(n):
            already_sorted = True
            for j in range(n - i - 1):
                if self[j] > self[j + 1]:
                    self[j], self[j + 1] = self[j + 1], self[j]
                    already_sorted = False
            if already_sorted:
                break
        if not ascending:  #it's descending
            self.index_based_reverse_order()

class InsertionSortMixin:
    """Mixin class providing insertion sort functionality for data structures."""
    def index_based_insertion_sort(self):
        """Sorts the elements of the data structure using the insertion sort algorithm with index-based access.

        This method is suitable for short lists or lists that are mostly sorted.

        Raises:
            TypeError: If the data structure does not support index-based access.

        Examples:
            >>> raarray = RandomAccessArray([2, 4, 5, 6, 8])
            >>> raarray
            RandomAccessArray([2, 4, 5, 6, 8])

            >>> raarray = RandomAccessArray(5)
            >>> [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            [None, None, None, None, None]

            >>> raarray.index_based_insertion_sort()
            >>> raarray
            RandomAccessArray([2, 4, 5, 6, 8])

        Notes:
            - The method modifies the original data structure in place.
            - Time Complexity: O(n^2), where n is the number of elements in the data structure.
        """
        if '__getitem__' not in dir(self):
            raise TypeError("index_based_insertion_sort can only be used on data structures that support index-based access.")
        for unsorted in range(1, len(self)):
            value = self[unsorted]  # persist the value found using the first key, `i`.
            j = unsorted - 1  # compute the first index of the sorted subarray
            while j >= 0 and value < self[j]:
                self[j + 1] = self[j]  # shift the value of the sorted subarray one to the right
                j -= 1  # compute the next index of the sorted subarray
            self[j + 1] = value  # insert the value one to the right of the minimum value

    #def reference_based_insertion_sort(self):
        """
        The outer loop traverses the entire singly linked list, except
        for the head. The outer loop sets `j` to the head during each
        iteration. `j` is used to traverse the sorted portion of the
        singly linked list until it reaches the current node. `j` provides
        the node to which compare the current node. The outer loop ends
        with advancing `prev` and `current` down the singly linked list.
        Summary: The outer loop resets `j` to the first sorted node, i.e.,
        `head` and advances `prev` and `current` down the singly linked
        list.

        The inner loop exits with either `j` is `current` or `j` is the node
        that should point to the current node.

        If `j` is current then current is in its sorted place and advance
        to the next unsorted node.

        If `j` is not current then `j` should point to `current`. The node `current`
        persists in the key `current` after it's bypassed in, i.e., removed from,
        the referenced-based structure.
            - Every time that a node Falsifies `j.next.data < current.data`,
            then `j` is the node that should point to the current node. So,
            every time we bypass `current` in the structure. `current` is bypassed
            but available in `current` until we reassign `current`.


        If `j` should point to the head of the reference-based object, point
        `current` at the head and leverage the head setter to insert `current`
        at the new head. In other words, change `current._next` to the old head
        and then use the reference-based object's managed `head` attribute to
        set the new head, i.e., current. Current has been sorted and now should
        be advanced to the next unsorted node.
        """
        if 'head' not in dir(self):
            raise TypeError("insertion_sort can only be used on reference-based data structures like linked lists.")
        if not self.head or not self.head.next:  # it's a zero node or one node list
            raise ValueError("Cannot sort an empty or one node linked list.")

        prev = self.head
        current = self.head._next
        while current:  # traverse the unsorted portion
            j = self.head  # traverse the sorted portion
            while j is not current and j._next.data < current.data:  # `j` should not point to current
                j = j._next  # advance to next sorted node
            if j is not current:  # `j` should point to current
                prev._next = current._next  # point to the next unsorted node, bypass current node

                if j is self.head and j.data > current.data:  # the current node should point to old head
                    current._next = self.head  # point current at the head
                    self.head = current  # trigger setter to add new head
                else:  # it's some node between head and current that current should point to
                    current._next = j._next
                    j._next = current

                current = prev._next  # advance current to next unsorted node
            else: # `j` reached current implying `current` is sorted
                prev, current = current, current._next  # advance to next unsorted node

class ReverseOrderMixin:
    """Mixin class supporting node order reversal for linked node structures."""
    def reference_based_reverse_order(self):
        """Reverses the order of elements in the singly linked data structure.

        Returns:
            None: This method modifies the original linked list in place.

        Examples:
            >>> sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            >>> sllist.reference_based_reverse_order()
            >>> sllist
            SinglyLinkedList([5, 4, 6, 2, 8])

        Notes:
            - Time Complexity: O(n), where n is the number of elements in the linked list.
        """
        if 'head' not in dir(self):
            raise TypeError("reference_based_reverse_order can only be used on reference-based data structures like linked lists.")
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

    def index_based_reverse_order(self):
        """Reverses the order of elements in the index-based data structure.

        Returns:
            None: This method modifies the original data structure in place.

        Examples:
            >>> raarray = RandomAccessArray(5)
            >>> [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            [None, None, None, None, None]
            >>> raarray.index_based_reverse_order()
            >>> raarray
            RandomAccessArray([5, 4, 6, 2, 8])

        Notes:
            - Time Complexity: O(n), where n is the number of elements in the data structure.
        """
        if '__getitem__' not in dir(self):
            raise TypeError("index_based_reverse_order can only be used on data structures that support index-based access.")
        n = len(self)
        for i in range(n // 2):
            # Swap elements symmetrically across the middle
            self[i], self[n - i - 1] = self[n - i - 1], self[i]