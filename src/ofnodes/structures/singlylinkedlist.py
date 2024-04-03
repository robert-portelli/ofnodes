from typing import Optional, Any

from ofnodes.nodes.singlynode import SinglyNode


class SinglyLinkedList:

    def __init__(self) -> None:
        self._head: Optional[SinglyNode] = None
        self._tail: Optional[SinglyNode] = None

    @property
    def head(self):
        """Getter property for the head of the linked list.

        Returns:
            SinglyNode | None: The head of the linked list, or None if the list is empty.

        Notes:
            The `head` property allows access to the first node in the linked list.

        Examples:
>>> llist = SinglyLinkedList()
>>> llist
SinglyLinkedList(head=None, tail=None)
>>> llist.head = "first node"
>>> llist.head
SinglyNode(data='first node')
>>> assert llist.head is llist.tail
>>> assert llist.head.next is None
>>> llist
SinglyLinkedList(head=This node's data is 11 of type str., tail=This node's data is 10 of type str.)
>>> llist.head, llist.head.next, llist.tail
(SinglyNode(data='second node'), SinglyNode(data='first node'), SinglyNode(data='first node'))
llist.head = None
>>> llist.head = None
>>> llist.head, llist.head.next, llist.tail
(SinglyNode(data=None), SinglyNode(data='second node'), SinglyNode(data='first node'))
>>> llist.head.__dict__
{'_data': None, '_next': SinglyNode(data='second node')}
>>> llist.remove_head()
>>> llist.head.__dict__
{'_data': 'second node', '_next': SinglyNode(data='first node')}
        """
        return self._head

    @head.setter
    def head(self, value: SinglyNode | Any) -> None:
        match value:
            case SinglyNode():
                node = value
            case _:
                node = SinglyNode(value)

        match self._head:
            case None:
                self._head = node
                self._tail = node

            case self._head:
                node.next = self._head
                setattr(self, "_head", node)

    @head.deleter
    def head(self):
        raise AttributeError(
            f"{type(self).__name__}'s `head` attribute " "cannot be deleted."
        )

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value: SinglyNode | Any) -> None:

        match value:
            case SinglyNode():
                node = value
            case _:
                node = SinglyNode(value)

        match self._head:
            case None:
                setattr(self, "_head", node)
                setattr(self, "_tail", node)
            case self._head:
                if not getattr(self._head, "_next"):
                    # it's a one node list
                    setattr(self._head, "_next", node)
                    setattr(self, "_tail", node)
                    return
                # there're more than one node
                setattr(self._tail, "_next", node)
                setattr(self, "_tail", node)

    @tail.deleter
    def tail(self):
        raise AttributeError(
            f"{type(self).__name__}'s `tail` attribute " "cannot be deleted."
        )

    def __repr__(self) -> str:
        return f"{type(self).__name__}(head={self.head}, tail={self.tail})"

    def __str__(self) -> str:
        match self:
            case SinglyLinkedList(head=None, tail=None):
                return "This instance of SinglyLinkedList is empty."
            case SinglyLinkedList(head=head, tail=tail):
                if head is tail:
                    return "This instance of SinglyLinkedList has a single node."
                return "The head and tail are different nodes."

    def insert_head(self, data):
        """
        Inserts a new node with the provided data at the head of the linked list.

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
        >>> linked_list.head.__dict__
        {'_data': 'third node added as head via property', '_next': SinglyNode(data={'the second node': (42.0, True, SinglyNode(data='LGRW'))})}
        >>> llist = SinglyLinkedList()
        >>> list(llist.insert_head(f"{i} node") for i in range(1, 5))
        [None, None, None, None]
        >>> llist.head = "to be assigned to `SinglyNode.data` then `SinglyLinkedList.head`"
        >>> llist.head, llist.head.next, llist.tail
        (SinglyNode(data='to be assigned to `SinglyNode.data` then `SinglyLinkedList.head`'), SinglyNode(data='4 node'), SinglyNode(data='1 node'))
        """
        self.head = data  # trigger the head setter

    def insert_tail(self, data):
        """Inserts a new node with the provided data at the tail of the linked list.

        Args:
            data: The data to be inserted into the new node. If the data is already a
                `SinglyNode` object, it is inserted directly; otherwise, a new
                `SinglyNode` object is created with the provided data.

        Returns:
            None

        Raises:
            ~~RuntimeError: If the linked list is not properly initialized (unexpected
                condition where `self.tail` is `None`).~~

            `self.tail` can't be deleted from instance. It's data value can be written
            over, but the attribute persists.

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
        >>> linked_list.tail.__dict__
        {'_data': 'insert 3rd node via property', '_next': None}
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

    def search(self, target):
        if self._head:
            current_node = self._head
            while current_node:
                if current_node.data == target:
                    return True
                current_node = current_node.next
            return False
        raise ValueError("The list is empty")

    def remove_head(self):
        if self._head and self._head is self._tail:
            self._head = None
            self._tail = None
            return
        if self._head and self._head is not self._tail:
            self._head = self.head.next
            return
        raise ValueError("Cannot remove head from empty list")

    def remove_tail(self):
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

    def print_list(self) -> None:
        """traverse the linked list object and call
        print on each node's data attribute"""
        current_node = self._head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == "__main__":

    def second_to_last(llist):
        node = llist._head
        while getattr(node, "_next") and getattr(node._next, "_next"):
            if node.next.next is llist._tail:
                node = node.next
                break
            node = node.next

    def header():
        sllist = SinglyLinkedList()
        for i in range(1, 4):
            sllist.head = f"{i} node"

    def tailer():
        sllist = SinglyLinkedList()
        for i in range(1, 4):
            sllist.tail = f"{i} node"

    llist = SinglyLinkedList()
    for i in range(1, 11):
        llist.tail = f"{i} node"

    header()
    tailer()

    """
    nodes = [SinglyNode(f"{i} node") for i in range(1,42)]
    sllist = SinglyLinkedList()
    # or
    list(sllist.insert_tail(node) for node in nodes)

    ---
    linked_list = SinglyLinkedList()
    linked_list.
    nodes = [SinglyNode(string) for string in ["second tail", "third tail"]]
    list(linked_list.insert_tail(data) for data in ["second tail", ])



    list(linked_list.insert_tail(data) for data in ["second tail", {'third_tail': (True, 11, 7.34)}])
    linked_list.head, linked_list.head.next, linked_list.tail


    """
