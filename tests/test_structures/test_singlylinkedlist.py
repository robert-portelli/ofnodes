

import pytest
from ofnodes.structures.singlylinkedlist import SinglyLinkedList
from ofnodes.nodes.singlynode import SinglyNode


def test__init__():
    sllist = SinglyLinkedList()
    assert (
        sllist.head is None and
        sllist.tail is None and
        sllist.target is None
    )
    sllist = SinglyLinkedList(['foo', 42.0, True])
    assert (
        getattr(sllist.head, "data") == 'foo'
        and
        getattr(sllist.head.next, "data") == 42.0
        and
        getattr(sllist.tail, 'data') is True
    )

def test__add__():
    sllist = SinglyLinkedList()
    sllist + 'foo'
    assert sllist.head.data == 'foo'
    sllist + 'bar'
    assert sllist.tail.data == 'bar'

def test__repr__():
    sllist = SinglyLinkedList()
    assert (
        repr(sllist) == "SinglyLinkedList()"
    )
    sllist = SinglyLinkedList(['foo', 42.0, True])
    assert (
        repr(sllist) == "SinglyLinkedList(['foo', 42.0, True])"
    )

def test__str__():
    sllist = SinglyLinkedList()
    assert (
        str(sllist) == 'Empty Singly Linked List'
    )
    sllist = SinglyLinkedList(['foo', 42.0, True])
    assert (
        str(sllist) == 'foo -> 42.0 -> True'
    )

def test__dir__():
    sllist = SinglyLinkedList()
    dirr = ['__add__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
            '__format__', '__ge__', '__getattribute__', '__getstate__',
            '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
            '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
            '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
            '__slots__', '__str__', '__subclasshook__', '__weakref__', 'bubble_sort','cycle_detection', 'head', 'insert_after_target', 'insert_before_target',
            'insert_head', 'insert_tail', 'print_node_data', 'remove', 'remove_head',
            'remove_tail','reverse_order', 'search', 'tail', 'target']
    assert dir(sllist) == dirr

def test_head_property():
    def test_head_setter_and_getter():
        sllist = SinglyLinkedList()
        assert sllist.head is None
        sllist.head = 'a string'
        assert isinstance(sllist.head, SinglyNode)
        sllist.head = SinglyNode('b string')

    def test_head_deleter():
        sllist = SinglyLinkedList()
        with pytest.raises(AttributeError) as exc_info:
            del sllist.head

        assert (
            "cannot be deleted" in str(exc_info.value)
        )

    test_head_setter_and_getter()
    test_head_deleter()

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

def test_search():
    def test_invalid_target():
        llist = SinglyLinkedList()
        with pytest.raises(ValueError) as exc_info:
            llist.target = 'will error'
        assert "Cannot assign" in str(exc_info)
    def test_empty_list():
        llist = SinglyLinkedList()
        with pytest.raises(ValueError) as exc_info:
            llist.search("some target data")
        assert "Cannot search" in str(exc_info)
    def test_found_and_not_found():
        llist = SinglyLinkedList()
        list(llist.insert_tail(f"{i} node") for i in range(1, 5))
        assert llist.search("1 node") is True
        assert llist.search("42 node") is False

    test_invalid_target()
    test_empty_list()
    test_found_and_not_found()

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

def test_print_node_data(capsys):
    sllist = SinglyLinkedList()
    list(sllist.insert_tail(f"{i} node") for i in range(1, 5))

    # Call the print_node_data method
    sllist.print_node_data()

    # Capture the printed output
    captured = capsys.readouterr()

    # Verify the printed output matches the expected output
    expected_output = "1 node\n2 node\n3 node\n4 node\n"
    assert captured.out == expected_output

def test_insert_head():
    sllist = SinglyLinkedList()
    sllist.insert_head("string")
    assert sllist.head.data == "string"

def test_target():
    def test_empty_list():
        sllist = SinglyLinkedList()
        with pytest.raises(ValueError) as exc_info:
            sllist.target = 'will error'
        assert "Cannot assign" in str(exc_info)
    def test_deleter():
        sllist = SinglyLinkedList()
        with pytest.raises(AttributeError) as exc_info:
            del sllist.target
        assert "cannot be deleted" in str(exc_info)
    def test_unacceptable_data():
        sllist = SinglyLinkedList()
        sllist.head = 'a string'
        with pytest.raises(ValueError) as exc_info:
            sllist.target = ''
        assert "unacceptable" in str(exc_info)

    test_empty_list()
    test_deleter()
    test_unacceptable_data()

def test_insert_after_target():
    def test_insert_after_one_node():
        sllist = SinglyLinkedList(['foo'])
        sllist.insert_after_target('foo', 'bar')
        assert getattr(sllist.head, 'next') is getattr(sllist, 'tail')
        assert getattr(sllist.tail, 'data') == 'bar'
    def test_insert_after_between_two_nodes():
        sllist = SinglyLinkedList(['foo', 'bar'])
        sllist.insert_after_target('foo', 'between nodes')
        assert getattr(sllist.head.next, 'data') == 'between nodes'
    def test_traverse_insert_after_before_tail():
        sllist = SinglyLinkedList(['foo', 'bar', 'moo', 'shoe'])
        sllist.insert_after_target('moo', 'before tail')
        assert getattr(sllist.head.next.next.next, 'data') == 'before tail'
        assert getattr(sllist.tail, 'data') == 'shoe'
    def test_traverse_insert_after_tail():
        sllist = SinglyLinkedList(['foo', 'bar', 'moo', 'shoe'])
        sllist.insert_after_target('shoe', 'after tail')
        assert getattr(sllist.head.next.next.next, 'data') == 'shoe'
        assert getattr(sllist.tail, 'data') == 'after tail'
    def test_first_encounter():
        sllist = SinglyLinkedList(['foo', 'bar', 'bar'])
        first_encounter = getattr(sllist.head, 'next')
        sllist.insert_after_target('bar', 'biz')
        assert getattr(sllist.head, 'next') is first_encounter
        assert getattr(sllist.head.next.next, 'data') == 'biz'
    def test_no_target_match():
        sllist = SinglyLinkedList(['foo', 'bar'])
        assert sllist.insert_after_target('baz', 'new node') is False
    def test_no_target_match_empty_list():
        sllist = SinglyLinkedList()
        assert sllist.insert_after_target('baz', 'new node') is False

    test_insert_after_one_node()
    test_insert_after_between_two_nodes()
    test_traverse_insert_after_before_tail()
    test_traverse_insert_after_tail()
    test_first_encounter()
    test_no_target_match()
    test_no_target_match_empty_list()

def test_insert_before_target():
    def test_insert_before_head():
        sllist = SinglyLinkedList(['foo', 'bar'])
        sllist.insert_before_target('foo', 'before head')
        assert getattr(sllist.head, 'data') == 'before head'
        assert getattr(sllist.head.next, 'data') == 'foo'
    def test_traversal_before_tail():
        sllist = SinglyLinkedList(['foo', 'bar', 'baz'])
        sllist.insert_before_target('baz', 'before tail')
        assert getattr(sllist.tail, 'data') == 'baz'
        assert getattr(sllist.head.next.next, 'data') == 'before tail'
    def test_no_target_match():
        sllist = SinglyLinkedList(['foo', 'bar'])
        assert sllist.insert_before_target('baz', 'new node') is False
    def test_no_target_match_empty_list():
        sllist = SinglyLinkedList()
        assert sllist.insert_before_target('baz', 'new node') is False

    test_insert_before_head()
    test_traversal_before_tail()
    test_no_target_match()
    test_no_target_match_empty_list()

def test_remove():
    def test_empty_list():
        sllist = SinglyLinkedList()
        with pytest.raises(ValueError) as exc_info:
            sllist.target = 'will error'
        assert "Cannot assign" in str(exc_info)

    def test_one_node():
        sllist = SinglyLinkedList()
        sllist.head = 'a node'
        sllist.remove('a node')

    def test_two_nodes():
        sllist = SinglyLinkedList()
        sllist.head = 'a node'
        sllist.tail = 'b node'
        sllist.remove('b node')

    def test_many_nodes():
        sllist = SinglyLinkedList()
        list(sllist.insert_tail(f"{i} node") for i in range(1, 5))
        sllist.remove('3 node')
        assert sllist.head.next.next.data != '3 node'

    def test_remove_first_encounter():
        sllist = SinglyLinkedList(['foo', 'bar', 'bar'])
        first_encounter = sllist.head.next
        sllist.remove('bar')
        assert first_encounter is not sllist.tail

    test_empty_list()
    test_one_node()
    test_two_nodes()
    test_many_nodes()
    test_remove_first_encounter()

def test_cycle_detection():
    sllist = SinglyLinkedList([f"node {i}" for i in range(1,7)])
    # the ofnodes library doesn't create cycles
    assert sllist.tail.next is None
    assert sllist.cycle_detection() is False
    # the ofnodes library discourages cycle creation
    with pytest.raises(AttributeError) as exc_info:
        sllist.tail.next = sllist.head
    assert "Cannot set 'next' attribute directly." in str(exc_info)
    # bypass SinglyNode.next setter to artificially create cycle
    setattr(sllist.tail, '_next', sllist.head.next)
    assert sllist.tail.next is not None
    # if you find yourself unable to access the SinglyLinkedList
    # tail attribute and think the tail setter was bypassed,
    # you can use the cycle_detection:
    assert sllist.cycle_detection() is True

def test_bubble_sort():
    sllist = SinglyLinkedList([8, 2, 6, 4, 5])
    sllist.bubble_sort()
    assert repr(sllist) == 'SinglyLinkedList([2, 4, 5, 6, 8])'
    assert str(sllist) == '2 -> 4 -> 5 -> 6 -> 8'