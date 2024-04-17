import pytest
from ofnodes.nodes.singlynode import SinglyNode
from ofnodes.structures.singlylinkedlist import SinglyLinkedList

def test__init__(example_singly_node):
    empty_node = example_singly_node['empty_node']

    assert isinstance(empty_node, SinglyNode)
    assert (
        empty_node.data is None
        and
        empty_node.next is None
    )


def test__dir__():
    node = SinglyNode('a string')
    dirr = ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
            '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__',
            '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
            '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
            '__sizeof__', '__slots__', '__str__', '__subclasshook__', 'data', 'next']
    assert dir(node) == dirr


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

def test_next():
    sllist = SinglyLinkedList()
    sllist.head = "first"
    with pytest.raises(AttributeError) as exc_info:
        setattr(sllist.head, 'next', "second")
    assert "Cannot set 'next'" in str(exc_info)
