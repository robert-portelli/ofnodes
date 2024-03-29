import pytest
from ofnodes.structures.singlylinkedlist import SinglyLinkedList, SinglyNode


def test__init__(example_singly_linked_list):
    sllist = example_singly_linked_list['empty']
    assert (
        sllist.head is None
        and
        sllist.tail is None
    )



def test__repr__(example_singly_linked_list):
    llist1 = example_singly_linked_list['empty']
    llist2 = example_singly_linked_list['example']
    assert (
        repr(llist1)
        == "SinglyLinkedList(head=None, tail=None)"
        ""
        and
        repr(llist2)
        ==
        (
        "SinglyLinkedList(head=This node's data is 4 of type list.,"
        " tail=This node's data is of type function.)"
        )
    )



def test__str__(example_singly_linked_list):
    llist1 = example_singly_linked_list['empty']
    llist2 = example_singly_linked_list['example']
    llist3 = example_singly_linked_list['one']
    assert(
        str(llist1)
        ==
        "This instance of SinglyLinkedList is empty."
        and
        str(llist2)
        ==
        "The head and tail are different nodes."
        and
        str(llist3)
        ==
        "This instance of SinglyLinkedList has a single node."
    )


def test_insert_tail():
    sllist = SinglyLinkedList()
    assert sllist.head is None and sllist.tail is None
    sllist.insert_tail("a string")
    assert sllist.head == sllist.tail
    sllist.insert_tail(42)
    assert (
        repr(sllist.head) == "SinglyNode(data='a string')"
        and
        repr(sllist.tail) == "SinglyNode(data=42)"
    )
    assert (
        str(sllist.head) == "This node's data is 8 of type str."
        and
        str(sllist.tail) == "This node's data is of type int."
    )
    sllist = SinglyLinkedList()
    sllist.head = SinglyNode('a string')
    # Call insert_tail and expect it to raise RuntimeError
    with pytest.raises(RuntimeError) as exc_info:
        sllist.insert_tail(20)

    # Verify the error message if needed
    assert str(exc_info.value) == "Unexpected condition: self.tail is None"
