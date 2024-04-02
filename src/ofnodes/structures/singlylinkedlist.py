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

        # Ensure the next attribute of the new head node is set to the current head
        node.next = self._head

        # Update the head attribute to reference the new node
        self._head = node

        # If the linked list is empty, also update the tail attribute to reference the new node
        if not self._tail:
            self._tail = node


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

        node.next = None

        if not self._head:  # If the linked list is empty
            self._head = node
            self._tail = node
        else:
            if self._tail:  # Check if _tail is not None
                self._tail.next = node  # Update the current tail node to point to the new node
            self._tail = node  # Update the tail attribute to reference the new node

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
        if not self.head:  # If the list is empty
            raise ValueError("Cannot remove tail from empty list")

        if self.head is self.tail:  # If there is only one node
            # effectively remove the one node for an empty list
            self.head = None
            self.tail = None
            return

        # Traverse from the head to find the second-to-last node
        current = self.head
        while current.next and current.next.next:  # stop when the next node is the tail
            current = current.next

        # Update pointer to second to last node
        self.tail = current
        self.tail.next = None

    def print_list(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == "__main__":
    onenode = SinglyLinkedList()
    onenode.tail = ("first node")
    newp = SinglyLinkedList()
    onenode.remove_head()
    for i in range(0, 3):
        onenode.tail = f"{i} node"
