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
        sllist.head.data == 'foo'
        and
        sllist.head.next.data == 42.0
        and
        sllist.tail.data is True
    )

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
    dirr = ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
            '__format__', '__ge__', '__getattribute__', '__getstate__',
            '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
            '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
            '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
            '__slots__', '__str__', '__subclasshook__', 'head',
            'insert_head', 'insert_tail', 'print_node_data', 'remove', 'remove_head',
            'remove_tail', 'search', 'tail', 'target']
    assert dir(sllist) == dirr

def test_head_property():
    def test_head_setter_and_getter():
        sllist = SinglyLinkedList()
        assert sllist.head is None
        sllist.head = 'a string'
        assert isinstance(sllist.head, SinglyNode)
        assert getattr(sllist.head, 'data') == 'a string'
        sllist.head = SinglyNode(None)
        assert isinstance(sllist.head, SinglyNode)
        assert getattr(sllist.head, 'data') is None

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
            llist.search(None)
        assert "Data unacceptable" in str(exc_info)
    def test_empty_list():
        llist = SinglyLinkedList()
        llist.search("some target data")
        assert(
            llist.head is None and
            llist.tail is None and
            llist.target == 'some target data'
        )
    def test_found_and_not_found():
        llist = SinglyLinkedList()
        list(llist.insert_tail(f"{i} node") for i in range(1, 5))
        llist.search("1 node")
        assert llist.head is llist.target
        llist.search("42 node")
        assert type(llist.target) is str

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
        sllist.target = 'string data'
        assert sllist.target == 'string data'
    def test_no_match():
        sllist = SinglyLinkedList()
        sllist.head = '2 node'
        sllist.target = '3 node'
        assert sllist.target == '3 node'
    def test_match():
        sllist = SinglyLinkedList()
        list(sllist.insert_tail(f"{i} node") for i in range(1, 5))
        sllist.target = '4 node'
        assert sllist.tail is sllist.target
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
    test_no_match()
    test_match()
    test_deleter()
    test_unacceptable_data()

def test_remove():
    def test_empty_list():
        sllist = SinglyLinkedList()
        with pytest.raises(ValueError) as exc_info:
            sllist.remove(sllist.target)
        assert "is empty" in str(exc_info)

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
        assert getattr(sllist.head.next.next, 'data') != '3 node'


    test_empty_list()
    test_one_node()
    test_two_nodes()
    test_many_nodes()