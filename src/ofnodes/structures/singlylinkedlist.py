from typing import Optional

from ofnodes.nodes.singlynode import SinglyNode



class SinglyLinkedList:

    def __init__(self) -> None:
        self._head: Optional[SinglyNode] = None
        self._tail: Optional[SinglyNode] = None


    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value: SinglyNode) -> None:

        match value:
            case SinglyNode():
                self._head = value
            case _:
                self._head = SinglyNode(value)

    @head.deleter
    def head(self):
        msg = (
            f"{type(self).__name__}'s `head` attribute "
            "cannot be deleted."
        )
        print(msg)

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value: SinglyNode) -> None:

        match value:
            case SinglyNode():
                self._tail = value
            case _:
                self._tail = SinglyNode(value)

    @tail.deleter
    def tail(self):
        msg = (
            f"{type(self).__name__}'s `tail` attribute "
            "cannot be deleted."
        )
        print(msg)


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
        node = SinglyNode(data)  # setter logic
        if self.head:
            node.next = self.head
            self.head = node
        else:  # necessary else statement
            self.head = node
            self.tail = node  # if not self.tail else self.tail

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
        if isinstance(data, SinglyNode):
            node = data
        else:
            node = SinglyNode(data)  # Create a new node with the provided data

        if not self.head:  # If the linked list is empty
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.next = node  # Append the new node to the current tail node
                self.tail = node  # Update the tail attribute to reference the new node
            else:
                # Handle the case where self.tail is None (unexpected condition)
                raise RuntimeError("Unexpected condition: self.tail is None")

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
        if self.head:
            self.head = self.head.next
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
        while current.next is not None and current.next is not self.tail:
            current = current.next  # found second to last node

        # Update pointer to second to last node
        self.tail = current
        self.tail.next = None

    def print_list(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == "__main__":
    dictx = examples = {
        "list": [
            "cat",
            42,
            42.0,
            True,
        ],
        "dict": {
            0: "one",
            1: ("tuple", "dog"),
        },
        "string": "13 characters",
        "set": {
            "one",
            2,
            3.0,
            False,
            None,
        },
        "bytes": bytes(
            [
                65,
                66,
                67,
            ]
        ),
        "bytearray": bytearray(b"LGRW"),
        "range": range(0, 43),
    }
    more_exs = {
        "none": SinglyNode(None),
        "int": SinglyNode(42),
        "float": SinglyNode(42.0),
        "bool": SinglyNode(True),
        "func": SinglyNode(lambda x: str(x) * 2),  # : disable=W0108
    }
    example = {**dictx, **more_exs}
    sllist = SinglyLinkedList()
    list(sllist.insert_tail(node) for node in example.values())
