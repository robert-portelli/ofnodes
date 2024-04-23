from ofnodes.nodes.singlynode import SinglyNode

class Head:
    def __get__(self, instance, owner):
        """Descriptor for managing the head/top of a data structure.

        This descriptor provides getter, setter, and deleter methods for managing the
        head/top of a data structure. It encapsulates the logic related to setting,
        getting, and deleting the head/top element of the data structure.

        Attributes:
            None

        Examples:
            This descriptor can be used in various data structures, such as linked lists,
            stacks, queues, etc., to manage the head/top element.

            >>> class Stack:
            ...     head = Head()
            ...
            >>> stack = Stack()
            >>> stack.head = 42
            >>> stack.head
            42
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

class Tail:
    """Descriptor for managing the tail of a data structure.

    This descriptor provides getter, setter, and deleter methods for managing the
    tail of a data structure. It encapsulates the logic related to setting, getting,
    and deleting the tail node of the data structure.

    Attributes:
        None

    Examples:
        This descriptor can be used in various data structures, such as linked lists,
        stacks, queues, etc., to manage the tail/top element.

        >>> class SinglyLinkedList:
        ...     tail = Tail()
        ...
        >>> llist = SinglyLinkedList()
        >>> llist.tail = "first node"
        >>> llist.tail
        'first node'
    """

    def __get__(self, instance, owner):
        """Getter method for the tail of the data structure.

        Args:
            instance: An instance of the class where the descriptor is used.
            owner: The class that owns the instance.

        Returns:
            Any | None: The tail of the data structure, or None if the
                data structure is empty.

        Notes:
            The `tail` property allows access to the last node in the data structure.

        Examples:
            This method can be used in various data structures to retrieve the tail
            node.

            >>> llist = SinglyLinkedList()
            >>> llist.tail = "first node"
            >>> llist.tail
            'first node'
        """
        return instance._tail

    def __set__(self, instance, value):
        """Setter method for the tail of the data structure.

        Args:
            instance: An instance of the class where the descriptor is used.
            value: The value to be set as the tail.

        Returns:
            None

        Notes:
            Setting the `tail` property allows modification of the last node in the
            data structure.
        """
        if isinstance(value, SinglyNode):
            node = value
        else:
            node = SinglyNode(value)

        if instance._head is None:
            setattr(instance, "_head", node)
            setattr(instance, "_tail", node)
        else:
            setattr(instance._tail, "_next", node)
            setattr(instance, "_tail", node)

    def __delete__(self, instance):
        """Deleter method for the tail of the data structure.

        Args:
            instance: An instance of the class where the descriptor is used.

        Returns:
            None

        Raises:
            AttributeError: Deleting the `tail` attribute is not allowed.

        Examples:
            This method can be used in various data structures to delete the tail
            node.

            >>> llist = SinglyLinkedList()
            >>> del llist.tail
            AttributeError: The `tail` attribute cannot be deleted.
        """
        raise AttributeError(
            f"{type(instance).__name__}'s `tail` attribute cannot be deleted."
        )
