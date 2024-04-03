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





def test__repr__(example_singly_node):
    node_with_data = example_singly_node['example_node_1']
    assert (
        repr(node_with_data)
        ==
        "SinglyNode(data='a pytest fixture')"
    )



def test__str__with_not_type_sized(example_singly_node_without_type_sized):
    assert (
        str(SinglyNode(None))
        == "This node's data is of type NoneType."
    )
    assert (
        str(example_singly_node_without_type_sized['int'])
        == "This node's data is of type int."
        )
    assert (
        str(example_singly_node_without_type_sized['float'])
        == "This node's data is of type float."
        and
        str(example_singly_node_without_type_sized['bool'])
        == "This node's data is of type bool."
        and
        str(example_singly_node_without_type_sized['func'])
        == "This node's data is of type function."
    )

def test__str__with_type_sized(example_singly_node_type_sized):
    assert (
        str(example_singly_node_type_sized['list'])
        == "This node's data is 4 of type list."
        and
        str(example_singly_node_type_sized['dict'])
        == "This node's data is 2 of type dict."
        and
        str(example_singly_node_type_sized['string'])
        == "This node's data is 13 of type str."
        and
        str(example_singly_node_type_sized['set'])
        == "This node's data is 5 of type set."
        and
        str(example_singly_node_type_sized['bytes'])
        == "This node's data is 3 of type bytes."
        and
        str(example_singly_node_type_sized['bytearray'])
        == "This node's data is 4 of type bytearray."
        and
        str(example_singly_node_type_sized['range'])
        == "This node's data is 43 of type range."
    )

def test_next():
    sllist = SinglyLinkedList()
    sllist.head = "first"
    with pytest.raises(AttributeError) as exc_info:
        setattr(sllist.head, 'next', "second")
    assert "Cannot set 'next'" in str(exc_info)
