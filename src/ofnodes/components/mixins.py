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

class RemoveMixin:
    """Mixin class providing remove functionality for linked structures."""

    def remove(self, target_data):
        """Removes the first occurrence of a node with the specified target data from the linked structure.

        Args:
            target_data (Any | Node): The data or node to be removed from the linked structure.

        Raises:
            ValueError: If the linked structure is empty.

        Returns:
            None: This method does not return any value.

        Removes the first occurrence of a node with the specified target data from the linked structure.
        If the linked structure is empty, a ValueError is raised.

        If the target data is found in the linked structure:
        - If the target node is the head, the head of the linked structure is updated to the next node.
        - If the target node is the tail, the tail of the linked structure is updated to the previous node.
        - For any other node, the reference to the next node is adjusted to skip the target node.

        Notes:
            This method removes only the first occurrence of the target data if multiple nodes contain the same data.

        Examples:
            >>> linked_structure = LinkedStructure()
            >>> list(linked_structure.insert_tail(f"{i} node") for i in range(1, 5))
            [None, None, None, None]
            >>> linked_structure.remove('0 node')
            >>> linked_structure.target
            '0 node'
            >>> linked_structure.head, linked_structure.head.next, linked_structure.tail
            (Node(data='1 node'), Node(data='2 node'), Node(data='4 node'))
            >>> linked_structure.remove('1 node')
            >>> linked_structure.target
            Node(data='1 node')
            >>> linked_structure.head, linked_structure.head.next, linked_structure.tail
            (Node(data='2 node'), Node(data='3 node'), Node(data='4 node'))
            >>> linked_structure.remove(linked_structure.tail)
            >>> linked_structure.target
            Node(data='4 node')
            >>> linked_structure.head, linked_structure.head.next, linked_structure.tail
            (Node(data='2 node'), Node(data='3 node'), Node(data='3 node'))
            >>> linked_structure.head.next
            Node(data='3 node')
            >>> linked_structure.tail
            Node(data='3 node')
            >>> linked_structure.remove(linked_structure.tail)
            >>> linked_structure.tail
            Node(data='2 node')
            >>> linked_structure.head.next
            >>> linked_structure.head, linked_structure.head.next, linked_structure.tail
            (Node(data='2 node'), None, Node(data='2 node'))
        """
        self.target = target_data  # trigger the setter

        if getattr(self._head, 'data') == self._target:
            self.remove_head()
            return

        current_node = self._head
        while current_node.next is not self._tail:
            if current_node.next.data == self._target:
                setattr(current_node, '_next', current_node.next.next)
                return
            current_node = current_node.next

        if getattr(self._tail, 'data') == self._target:
            self.remove_tail()
            return

    def remove_head(self) -> None:
        """Removes the head node from the linked structure.

            Raises:
                ValueError: If the linked structure is empty.

            Returns:
                None

            Notes:
                - If the head node is the only node in the list, both the head and tail references are set to None.
                - If the head node is not the only node, the head reference is updated to point to the next node.
                TODO: overload `-` operator to support:
                        1) `linked_structure - linked_structure.head`
                        2) `linked_structure - linked_structure.tail`
                        3) `linked_structure - linked_structure.spot()`

            Examples:
                >>> linked_structure = LinkedStructure()
                >>> linked_structure
                LinkedStructure(head=None, tail=None)
                >>> linked_structure.head = {42: "a string"}
                >>> linked_structure
                LinkedStructure(head=Node(data='1 node'), tail=Node(data='1 node'))
                >>> linked_structure.head.data[42]
                'a string'
                >>> linked_structure.remove_head()
                >>> linked_structure
                LinkedStructure(head=None, tail=None)
        """
        if self._head and self._head is self._tail:
            self._head = None
            self._tail = None
            return
        if self._head and self._head is not self._tail:
            self._head = self._head.next
            return
        raise ValueError("Cannot remove head from empty list")

    def remove_tail(self) -> None:
        """Removes the tail node from the linked structure.

        Raises:
            ValueError: If the linked structure is empty.

        Returns:
            None

        Examples:
            >>> linked_structure = LinkedStructure()
            >>> linked_structure
            LinkedStructure(head=None, tail=None)
            >>> linked_structure.head = True
            >>> linked_structure
            LinkedStructure(head=Node(data=True), tail=Node(data=True))
            >>> linked_structure.tail = ['strings', Node(lambda x: str(x)*2)]
            >>> linked_structure
            LinkedStructure(head=Node(data=True), tail=Node(data=['strings', Node(data=<function <lambda> at 0x74a9932a2fc0>)]))
            >>> linked_structure.tail
            Node(data=['strings', Node(data=<function <lambda> at 0x74a9932a2fc0>)])
            >>> linked_structure.tail.data[1].data
            <function <lambda> at 0x74a9932a2fc0>
            >>> x = linked_structure.tail.data[1].data
            >>> x("skrrt")
            'skrrtskrrt'
            >>> linked_structure.remove_tail()
            >>> x("skrrt")
            'skrrtskrrt'
            >>> linked_structure.tail
            Node(data=True)
            """
        match self._head:
            case None:
                raise ValueError("Cannot remove tail from empty list")
            case self._head:
                if not getattr(self._head, "_next"):
                    # it's a one node list
                    setattr(self, "_head", None)
                    setattr(self, "_tail", None)
                    return
                if getattr(self._head, "next") is self._tail:
                    # there are two nodes
                    setattr(self, "_tail", self._head)
                    setattr(self._tail, "_next", None)
                    return
                # there are more than two nodes
                node = self._head
                # find second to last node
                while getattr(node, "_next") and getattr(node._next, "_next"):
                    if getattr(node._next, "_next") is self._tail:
                        node = getattr(node, "_next")  # target found
                        break
                    node = getattr(node, "_next")  # keep looking
                setattr(node, "_next", None)  # point the second to last node to None
                setattr(self, "_tail", node)  # assign tail to the node

class PrintMixin:
        """Mixin class providing node data print functionality"""
        def print_node_data(self) -> None:
            """Traverse the linked data structure and print the data attribute of each node.

            Returns:
                None

            Notes:
                This method iterates through the linked data structure starting from the head node and prints the data attribute of each node
                until the end of the linked structure is reached.

            Examples:
                >>> sllist = SinglyLinkedList()
                >>> list(sllist.insert_tail(f"{i} node") for i in range(1, 5))
                [None, None, None, None]
                >>> sllist.head
                SinglyNode(data='1 node')
                >>> sllist.tail
                SinglyNode(data='4 node')
                >>> sllist.print_node_data()
                1 node
                2 node
                3 node
                4 node
            """
            current_node = self._head
            while current_node:
                print(current_node.data)
                current_node = current_node.next