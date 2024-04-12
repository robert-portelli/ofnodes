import pytest
from ofnodes.structures.singlylinkedlist import SinglyLinkedList
from ofnodes.nodes.singlynode import SinglyNode


def test__init__(example_singly_linked_list):
    sllist = example_singly_linked_list['empty']
    assert (
        sllist.head is None
        and
        sllist.tail is None
    )


def test__repr__():
    llist = SinglyLinkedList()
    assert (
        repr(llist)
        ==
        "SinglyLinkedList(head=None, tail=None, target=None)"
    )
    llist.head = 42
    llist.tail = 'a string'
    llist.target = 'b string'
    assert (
        repr(llist)
        ==
        (
            "SinglyLinkedList(head=This node's data is of type int., "
            "tail=This node's data is 8 of type str., target=b string)"
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
    
def test_data_setter():
    node = SinglyNode(data=42)
    assert node.data == 42
    node.data = "a string"
    assert node.data == "a string"


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

def test_head_setter():
    sllist = SinglyLinkedList()
    sllist.head = "first head"
    sllist.head = SinglyNode("second head")


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
    def test_invalid_target():
        llist = SinglyLinkedList()
        with pytest.raises(ValueError) as exc_info:
            llist.search(None)
        assert "unable to be target" in str(exc_info)
    def test_empty_list():
        llist = SinglyLinkedList()
        with pytest.raises(ValueError) as exc_info:
            llist.search("target")
        assert "list is empty" in str(exc_info)
    def test_list():
        llist = SinglyLinkedList()
        for i in range(0, 3):
            llist.tail = f"{i} node"
        assert llist.search("2 node")
        assert not llist.search("42 node")

    test_invalid_target()
    test_empty_list()
    test_list()

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

def test_target(capsys):
    def test_empty_list():
        sllist = SinglyLinkedList()
        sllist.target = None
        captured = capsys.readouterr()
        expected_output = "Empty `SinglyLinkedList()`. Target data is assigned to SinglyLinkedList's target property.\n"
        assert expected_output == captured.out
    def test_no_match():
        sllist = SinglyLinkedList()
        sllist.head = '2 node'
        sllist.target = '3 node'
        captured = capsys.readouterr()
        expected_output = f"""No target matches. Target data assigned to {type(sllist).__name__}'s target property.\n"""
        assert expected_output == captured.out
    def test_match():
        sllist = SinglyLinkedList()
        list(sllist.insert_tail(f"{i} node") for i in range(1, 5))
        sllist.target = '3 node'
        assert sllist.head.next.next is sllist.target
    def test_deleter():
        sllist = SinglyLinkedList()
        with pytest.raises(AttributeError) as exc_info:
            del sllist.target
        assert "cannot be deleted" in str(exc_info)


    test_empty_list()
    test_no_match()
    test_match()
    test_deleter()

def test_remove():
    def test_empty_list():
        sllist = SinglyLinkedList()
        # TODO

    def test_one_node():
        sllist = SinglyLinkedList()
        # TODO

    test_empty_list()
    test_one_node()