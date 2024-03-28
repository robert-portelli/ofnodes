import pytest

from ofnodes.nodes.singlynode import SinglyNode
from ofnodes.structures.singlylinkedlist import SinglyLinkedList


@pytest.fixture
def example_singly_node():
    return SinglyNode("a pytest fixture")


@pytest.fixture
def example_singly_node_without_type_sized():
    """The SinglyLinkedNode __str__() displays a message
    depending on the data it holds.
    The type hints will warn you about calling `len()`
    on a type that could lack `__len__`.
    Below are Singly Linked Nodes with data lacking __len__.
    """
    return {
        "none": SinglyNode(None),
        "int": SinglyNode(42),
        "float": SinglyNode(42.0),
        "bool": SinglyNode(True),
        "func": SinglyNode(lambda x: str(x)),  # pylint: disable=W0108
    }


@pytest.fixture
def example_singly_node_type_sized():
    """The SinglyLinkedNode __str__() displays a message
    depending on the data it holds.
    The type hints will warn you about calling `len()`
    on a type that could lack `__len__`.
    Below are Singly Linked Nodes with data having __len__.
    """
    examples = {
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
    return {key: SinglyNode(value) for key, value in examples.items()}


@pytest.fixture
def example_singly_linked_list():
    nodes = {
        **example_singly_node_type_sized(),
        **example_singly_node_without_type_sized(),
    }
    sllist = SinglyLinkedList()
    sllist.insert_tail(nodes["empty"])
    return {
        "empty": sllist,
        "not_empty": sllist.insert_tail(list(nodes.values())),
    }
