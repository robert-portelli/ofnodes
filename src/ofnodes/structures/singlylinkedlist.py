from typing import Optional, Any

from ofnodes.nodes.singlynode import SinglyNode
from ofnodes.components.descriptors import Head, Tail, Target
from ofnodes.components.mixins import SearchMixin, RemoveMixin, PrintMixin

class SinglyLinkedList(SearchMixin, RemoveMixin, PrintMixin):
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

    def insert_head(self, data: Any) -> None:
        """ Inserts a new node with the provided data at the head of the linked list.

        Args:
            data: The data to be inserted into the new node. If the data is already a
                `SinglyNode` object, it is inserted directly; otherwise, a new
                `SinglyNode` object is created with the provided data.

        Returns:
            None

        Notes:
            If the linked list is empty, the new node becomes both the head and the
            tail of the linked list. If the linked list is not empty, the new node
            is inserted at the beginning of the list by updating the `next` attribute
            of the new node to point to the current head node, and then updating the
            instance's `head` attribute to reference the new node.

        Examples:
            >>> linked_list = SinglyLinkedList()
            >>> linked_list
            SinglyLinkedList(head=None, tail=None)
            >>> linked_list.insert_head("the first node in the list")
            >>> assert linked_list.head is linked_list.tail
            >>> linked_list.insert_head({"the second node": (42.0, True, SinglyNode("LGRW"))})
            >>> assert (
            ...     linked_list.head is not linked_list.tail
            ...     and
            ...     linked_list.head.next is linked_list.tail
            ... )
            >>> linked_list.head, linked_list.tail
            (SinglyNode(data={'the second node': (42.0, True, SinglyNode(data='LGRW'))}), SinglyNode(data='the first node in the list'))
            >>> linked_list.head = "third node added as head via property"
            >>> linked_list.head, linked_list.tail
            (SinglyNode(data='third node added as head via property'), SinglyNode(data='the first node in the list'))
            >>> llist = SinglyLinkedList()
            >>> list(llist.insert_head(f"{i} node") for i in range(1, 5))
            [None, None, None, None]
            >>> llist.head = "to be assigned to `SinglyNode.data` then `SinglyLinkedList.head`"
            >>> llist.head, llist.head.next, llist.tail
            (SinglyNode(data='to be assigned to `SinglyNode.data` then `SinglyLinkedList.head`'), SinglyNode(data='4 node'), SinglyNode(data='1 node'))
        """
        self.head = data  # trigger the head setter

    def insert_tail(self, data: Any) -> None:
        """Inserts a new node with the provided data at the tail of the linked list.

        Args:
            data: The data to be inserted into the new node. If the data is already a
                `SinglyNode` object, it is inserted directly; otherwise, a new
                `SinglyNode` object is created with the provided data.

        Returns:
            None

        Notes:
            If the linked list is empty, the new node becomes both the head and the
            tail of the linked list. Otherwise, the new node is appended to the end
            of the list by updating the `next` attribute of the current tail node
            to point to the new node, and then updating the instance's `tail`
            attribute to reference the new node.

        Examples:
            >>> linked_list = SinglyLinkedList()
            >>> linked_list
            SinglyLinkedList(head=None, tail=None)
            >>> linked_list.insert_tail("the first node in a list")
            >>> assert linked_list.head is linked_list.tail
            >>> linked_list.head, linked_list.head.next, linked_list.tail
            (SinglyNode(data='the first node in a list'), None, SinglyNode(data='the first node in a list'))
            >>> linked_list.insert_tail({"the second node": (42.0, True, SinglyNode("LGRW"))})
            >>> linked_list.head, linked_list.head.next, linked_list.tail
            (SinglyNode(data='the first node in a list'), SinglyNode(data={'the second node': (42.0, True, SinglyNode(data='LGRW'))}), SinglyNode(data={'the second node': (42.0, True, SinglyNode(data='LGRW'))}))
            >>> assert linked_list.head is not linked_list.tail
            >>> assert linked_list.head.next is linked_list.tail
            >>> linked_list.tail
            SinglyNode(data={'the second node': (42.0, True, SinglyNode(data='LGRW'))})
            >>> linked_list.tail.data['the second node']
            (42.0, True, SinglyNode(data='LGRW'))
            >>> linked_list.tail.data['the second node'][2].data
            'LGRW'
            >>> linked_list.tail = "insert 3rd node via property"
            >>> linked_list.tail.data
            'insert 3rd node via property'
            >>> llist = SinglyLinkedList()
            >>> list(llist.insert_tail(f"{i} node") for i in range(1, 5))
            >>> llist.head, llist.head.next, llist.tail
            (SinglyNode(data='1 node'), SinglyNode(data='2 node'), SinglyNode(data='4 node'))
            >>> llist.tail = "is passed to setter to become SinglyNode()"
            >>> llist.head, llist.head.next, llist.tail
            (SinglyNode(data='1 node'), SinglyNode(data='2 node'), SinglyNode(data='is passed to setter to become SinglyNode()'))
        """
        self.tail = data  # trigger the tail setter

    def insert_after_target(self, target_data: Any, data_to_insert: Any) -> bool:
        """
        Inserts a new node containing the specified data after the first occurrence
        of the target data in the linked list.

        Args:
            target_data (Any): The data value to search for in the linked list.
            data_to_insert (Any): The data value to insert after the target data.

        Returns:
            bool: True if the insertion was successful, False otherwise.

        Raises:
            ValueError: If the target data is not found in the linked list.

        Note:
            This method triggers the setter for the target data attribute.
            If the target data is found at the head of the linked list and the list
            contains only one node, the new node becomes the new tail of the list.
            Otherwise, the method traverses the list to find the target data and inserts
            the new node immediately after it. If the target data is found at the tail,
            the new node becomes the new tail of the list.
        """
        try:
            self.target = target_data  # trigger the setter
        except ValueError:
            return False
        # check head and if it's a one node list
        if self._head and self._head.data == self._target:
            if self._head is self._tail:  # it's a one node list
                self.tail = data_to_insert  # trigger the setter, tail property will validate input
                return True

        # check each node in the list from head until, but not including, the tail
        current_node = self._head
        while current_node and current_node is not self._tail:  # traversal
            if current_node.data == self._target:
                new_node = SinglyNode(data_to_insert)  # SinglyNode() will validate input
                setattr(new_node, '_next', current_node.next)  # insert after()
                setattr(current_node, '_next', new_node)  # insert after()
                return True
            current_node = current_node.next  # traversal
        # check tail
        if getattr(self._tail, 'data') == self.target:
            self.tail = data_to_insert  # # trigger the setter, tail property will validate input
            return True
        # no target match
        return False

    def insert_before_target(self, target_data: Any, data_to_insert: Any) -> bool:
        """
        Inserts a new node containing the specified data before the first occurrence
        of the target data in the linked list.

        Args:
            target_data: The data value to search for in the linked list or the reference to the node.
            data_to_insert: The data value to insert before the target data.

        Returns:
            bool: True if the insertion was successful, False otherwise.

        Raises:
            ValueError: If the target data is not found in the linked list.

        Note:
            This method assumes that the linked list has already been instantiated.
            If the target data is found at the head of the linked list, the new node
            will become the new head of the list.

        Examples:
            >>> sllist = SinglyLinkedList(['foo', 'bar'])
            >>> sllist.insert_before_target('foo', 'before_head')
            True
            >>> sllist
            SinglyLinkedList(['before_head', 'foo', 'bar'])

            >>> sllist.insert_before_target('baz', 'new node')
            False
            >>> sllist
            SinglyLinkedList(['before_head', 'foo', 'bar'])

            >>> sllist.insert_before_target(sllist.head, 'new node')
            True
            >>> sllist
            SinglyLinkedList(['new node', 'before_head', 'foo', 'bar'])
        """
        try:
            self.target = target_data  # trigger the setter
        except ValueError:
            return False
        current_node = getattr(self, '_head')
        while current_node and current_node.next: # traversal
            # check head
            if current_node.data == self._target:
                self.head = data_to_insert  # trigger the setter, head property will validate input
                return True
            # check after head through tail
            if current_node.next.data == self._target:  # peek
                new_node = SinglyNode(data_to_insert)  # SinglyNode() will validate data_to_insert
                setattr(new_node, '_next', current_node.next)  # insert_before()
                setattr(current_node, '_next', new_node)  # insert before()
                return True
            current_node = getattr(current_node, 'next')  # traversal
        return False
