from typing import Optional, Any

from ofnodes.nodes.singlynode import SinglyNode



class SinglyLinkedList:

    def __init__(self) -> None:
        self._head: Optional[SinglyNode] = None
        self._tail: Optional[SinglyNode] = None

    @property
    def head(self):
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
                setattr(self, '_head', node)

    @head.deleter
    def head(self):
        raise AttributeError(
            f"{type(self).__name__}'s `head` attribute "
            "cannot be deleted."
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
                setattr(self, '_head', node)
                setattr(self, '_tail', node)
            case self._head:
                if not getattr(self._head, '_next'):
                    # it's a one node list
                    setattr(self._head, '_next', node)
                    setattr(self, '_tail', node)
                    return
                # there're more than one node
                setattr(self._tail, '_next', node)
                setattr(self, '_tail', node)



    @tail.deleter
    def tail(self):
        raise AttributeError(
            f"{type(self).__name__}'s `tail` attribute "
            "cannot be deleted."
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
        """this is implemented by the .head property"""
        self.head = data

    def insert_tail(self, data):
        """Inserts a new node with the provided data at the tail of the linked list.

        Args:
            data: The data to be inserted into the new node. If the data is already a
                `SinglyNode` object, it is inserted directly; otherwise, a new
                `SinglyNode` object is created with the provided data.

        Returns:
            None

        Raises:
            RuntimeError: If the linked list is not properly initialized (unexpected
                condition where `self.tail` is `None`).

        Notes:
            If the linked list is empty, the new node becomes both the head and the
            tail of the linked list. Otherwise, the new node is appended to the end
            of the list by updating the `next` attribute of the current tail node
            to point to the new node, and then updating the instance's `tail`
            attribute to reference the new node.

        Examples:
            >>> linked_list = SinglyLinkedList()
            >>> linked_list.insert_tail(10)
            >>> linked_list.insert_tail(SinglyNode(20))
        """
        # This is self.data setter validation
        self.tail = data

    def search(self, target):
        if self.head:
            current_node = self.head
            while current_node:
                if current_node.data == target:
                    return True
                current_node = current_node.next
            return False
        raise ValueError("The list is empty")

    def remove_head(self):
        if self.head and self.head is self.tail:
            self._head = None
            self._tail = None
            return
        if self.head and self.head is not self.tail:
            self._head = self.head.next
            return
        raise ValueError("Cannot remove head from empty list")

    def remove_tail(self):
        """Traverse the uni linked list to find the second-to-last node"""
        if self._head is None:  # If the list is empty
            raise ValueError("Cannot remove tail from empty list")

        if self._head is self._tail:  # If there is only one node
            # effectively remove the one node for an empty list
            #self.head = None
            #self.tail = None
            setattr(self, 'head', None)
            setattr(self, 'tail', None)

        if self._head.next is self._tail:  # there are only two nodes
            #self._tail = self._head
            #self._tail.next = None
            setattr(self, '_tail', self._head)
            setattr(self._tail, 'next', None)

        # Traverse from the head to find the second-to-last node
        current = self._head
        while current.next and current.next.next:  # stop when the next node is the tail
            if current.next.next is self._tail:
                current = current.next
                break
            current = current.next

        setattr(current, 'next', None)
        #self.tail = current
        setattr(self, 'tail', current)

    def print_list(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == "__main__":
    #sllist = SinglyLinkedList()
    #for i in range(0, 3):
    #    sllist.tail = f"{i} node"
    #header = SinglyLinkedList()

    #header.head = "a head string"
    #tailer.tail = "first tail node"
    #tailer.tail = "new tail node"
    def header():
        sllist = SinglyLinkedList()
        for i in range(1, 4):
            sllist.head = f"{i} node"
    def tailer():
        sllist = SinglyLinkedList()
        for i in range(1, 4):
            sllist.tail = f"{i} node"
