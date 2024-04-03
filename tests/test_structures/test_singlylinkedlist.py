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

def test_head_setter():
    node = SinglyNode('string for data')
    data = 'input was str not node'
    def head_attribute():
        llist = SinglyLinkedList()
        llist.head = node
        assert llist.head == node
        llist.head = data
        assert isinstance(llist.head, SinglyNode)
        assert llist.head.data == 'input was str not node'
    def insert_head_method():
        llist = SinglyLinkedList()
        llist.insert_head(node)
        assert llist.head == node
        assert llist.tail == node
        #assert getattr(llist.head, 'next') is None
        llist.insert_head(data)
        assert (
            getattr(llist.head, 'data') is data
        )
        assert (
            isinstance(llist.head, SinglyNode)
        )
        assert getattr(llist.head, 'next') is node
        #assert

    head_attribute()
    insert_head_method()

def test_head_deleter(example_singly_linked_list):
    llist = example_singly_linked_list['one']
    # Act & Assert
    with pytest.raises(AttributeError) as exc_info:
        del llist.head

    assert (
        "cannot be deleted" in str(exc_info.value)
    )


def test_tail_setter():
    """
    The tail setter accepts SinglyNodes any Any data type.
    Any data type is used to create a SinglyNode of the data
    before being set as the tail value."""
    sllist = SinglyLinkedList()
    assert sllist.head is None and sllist.tail is None
    node = SinglyNode("a string")
    tup = (42, ['this', True])
    sllist.tail = node
    assert (
        sllist.head == node
        and
        sllist.tail == node
        and
        sllist.head is sllist.tail
    )

    sllist.tail = tup  # trigger tail setter

    assert (
        sllist.head is not sllist.tail
        and
        sllist.head == node
        and
        isinstance(sllist.tail, SinglyNode)
        and
        sllist.tail.data == tup
    )

def test_tail_deleter(example_singly_linked_list):
    llist = example_singly_linked_list['one']
    with pytest.raises(AttributeError) as exc_info:
        del llist.tail

    assert (
        "cannot be deleted" in str(exc_info.value)
    )

def test_remove_head(easy_singly_linked_list):
    def test_error():
        llist = SinglyLinkedList()
        assert llist.head is None
        with pytest.raises(ValueError) as exc_info:
            llist.remove_head()
        assert "Cannot remove" in str(exc_info)

    def test_logic():
        llist = easy_singly_linked_list
        old_head = llist.head
        old_head_next = llist.head.next
        llist.remove_head()
        assert old_head is not llist.head
        assert old_head_next is not llist.head.next
        assert old_head_next is llist.head
        llist.remove_head()
        assert llist.head and llist.head is llist.tail
        llist.remove_head()
        assert not llist.head and not llist.tail


    test_error()
    test_logic()

def test_search(example_singly_linked_list):
    llist = SinglyLinkedList()
    with pytest.raises(ValueError) as exc_info:
        llist.search("target")
    assert "list is empty" in str(exc_info)
    for i in range(0, 3):
        llist.tail = f"{i} node"
    assert llist.search("2 node")
    assert not llist.search("42 node")

def test_remove_tail():
    def test_short_list():
        nodes = [SinglyNode(f"{i} node") for i in range(1,4)]
        sllist = SinglyLinkedList()
        # list(setattr(sllist, 'tail', node) for node in nodes)
        list(sllist.insert_tail(node) for node in nodes)
        assert nodes[-1] is sllist.tail
        sllist.remove_tail()
        assert (
            nodes[-1] is not sllist.tail
            and
            nodes[-2] is sllist.tail
        )
        sllist.remove_tail()
        assert (
            nodes[-2] is not sllist.tail
            and
            nodes[0] is sllist.tail
            and
            nodes[0] is sllist.head
        )
        sllist.remove_tail()
        assert(
            sllist.head is None
            and
            sllist.tail is None
        )
        with pytest.raises(ValueError) as exc_info:
            sllist.remove_tail()
        assert "Cannot remove tail" in str(exc_info)

    def test_long_list():
        """tests the 'find the second to last node'
        functionality"""
        nodes = [SinglyNode(f"{i} node") for i in range(1,42)]
        sllist = SinglyLinkedList()
        list(setattr(sllist, 'tail', node) for node in nodes)
        assert nodes[-1] is sllist.tail
        sllist.remove_tail()
        assert nodes[-2] is sllist.tail

    test_short_list()
    test_long_list()
