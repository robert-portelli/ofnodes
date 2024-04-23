from ofnodes.nodes.singlynode import SinglyNode

class Head:
    def __get__(self, instance, owner):
        """Getter method for the head/top of the data structure.

        Args:
            instance: An instance of the class where the descriptor is used.
            owner: The class that owns the instance.

        Returns:
            Any | None: The head/top element of the data structure, or None if the
                data structure is empty.

        Notes:
            The `head` property allows access to the top element of the data structure.

        Raises:
            None

        Examples:
            This method can be used in various data structures to retrieve the head/top
            element.

            >>> llist = SinglyLinkedList()
            >>> llist.head = SinglyNode(42)
            >>> llist.head
            SinglyNode(data=42)
        """
        return instance._head

    def __set__(self, instance, value):
        """Setter method for the head/top of the data structure.

        Args:
            instance: An instance of the class where the descriptor is used.
            value: The value to be set as the head/top element.

        Returns:
            None

        Raises:
            None

        Examples:
            This method can be used in various data structures to set the head/top
            element.

        Examples:
            >>> llist = SinglyLinkedList()
            >>> llist.head = SinglyNode(42)
            >>> llist.head
            SinglyNode(data=42, next=None)
        """
        if isinstance(value, SinglyNode):
            node = value
            #return
        else:
            node = SinglyNode(value)

        if instance._head is None:
            instance._head = node
            instance._tail = node
        else:
            setattr(node, '_next', instance._head)
            instance._head = node

    def __delete__(self, instance):
        """Deleter method for the head/top of the data structure.

        Args:
            instance: An instance of the class where the descriptor is used.

        Returns:
            None

        Raises:
            AttributeError: Deleting the `head` attribute is not allowed.

        Examples:
            This method can be used in various data structures to delete the head/top
            element.

        Examples:
            >>> llist = SinglyLinkedList()
            >>> del llist.head
            AttributeError: SinglyLinkedList's `head` attribute cannot be deleted.
        """
        raise AttributeError(
            f"{type(instance).__name__}'s `head` attribute " "cannot be deleted."
        )