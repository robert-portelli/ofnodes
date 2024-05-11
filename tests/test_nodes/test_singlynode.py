import pytest
from ofnodes.nodes.singlynode import SinglyNode
from ofnodes.structures.singlylinkedlist import SinglyLinkedList

def test_dynamic_attribute_assignment():
    node = SinglyNode(42)
    with pytest.raises(AttributeError) as exc_info:
        node.fail = True
    assert "object has no attribute" in str(exc_info)
test_dynamic_attribute_assignment()

def test__init__(example_singly_node):
    empty_node = example_singly_node['empty_node']

    assert isinstance(empty_node, SinglyNode)
    assert (
        empty_node.data is None
        and
        empty_node.next is None
    )

def test__add__():
    def test_expected():
        node = SinglyNode('foo')
        node + ' bar'
        assert str(node) == 'foo bar'
        node = SinglyNode(42)
        node + 42
        assert node.data == 84
    def test_error():
        node = SinglyNode('foo')
        with pytest.raises(ValueError) as exc_info:
            node + None
        assert "Invalid data" in str(exc_info)

    test_expected()
    test_error()

def test__dir__():
    node = SinglyNode('a string')
    dirr = ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
            '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__',
            '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
            '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
            '__sizeof__', '__slots__', '__str__', '__subclasshook__','data', 'next']
    assert dir(node) == dirr
    assert "__dict__" not in str(dir(node))


def test__repr__(example_singly_node):
    node_with_data = example_singly_node['example_node_1']
    assert (
        repr(node_with_data)
        ==
        "SinglyNode(data='a pytest fixture')"
    )

def test__str__():
    node = SinglyNode('a string')
    assert str(node) == 'a string'

def test_next_property():
    def test_getter_and_setter():
        sllist = SinglyLinkedList()
        sllist.head = "first"
        with pytest.raises(AttributeError) as exc_info:
            setattr(sllist.head, 'next', "second")
        assert "Cannot set 'next'" in str(exc_info)

    def test_deleter():
        snode = SinglyNode(None)
        with pytest.raises(AttributeError) as exc_info:
            del snode.next
        assert "cannot be deleted" in str(exc_info)

    test_getter_and_setter()
    test_deleter()

def test_data_property():
    def test_getter_and_setter():
        snode = SinglyNode(None)
        assert getattr(snode, 'data') is None
        snode.data = 'a string'
        assert getattr(snode, 'data') == 'a string'

    def test_deleter():
        snode = SinglyNode(None)
        with pytest.raises(AttributeError) as exc_info:
            del snode.data
        assert "cannot be deleted" in str(exc_info)

    test_getter_and_setter()
    test_deleter()
