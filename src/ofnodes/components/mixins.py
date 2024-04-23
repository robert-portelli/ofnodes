class SearchMixin:
    """Mixin class providing search functionality for linked lists."""

    def search(self, target_data):
        """Searches each node's data in a linked list until the first occurrence of
        the target is found.

        Args:
            target_data (Any): The value to search for in the linked list.

        Returns:
            bool: True if the target value is found in the linked list, False otherwise.

        Raises:
            ValueError: If the linked list is empty.

        Notes:
            This method iterates through the linked list starting from the head node
            and checks each node's data value for equality with the target value.

        Examples:
            >>> llist = SinglyLinkedList()
            >>> llist.head = "first node"
            >>> llist.head = "second node"
            >>> llist.search("first node")
            True
            >>> llist.search(SinglyNode("first node"))
            False
            >>> llist.search("third node")
            False
            >>> llist.tail = "third node"
            >>> llist.search("third node")
            True
        """
        if self._head is None:
            raise ValueError("Cannot search an empty linked list.")

        current_node = self._head
        while current_node:
            if current_node.data == target_data:
                return True
            current_node = current_node.next
        return False
