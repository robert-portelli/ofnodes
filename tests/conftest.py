import pytest
from typing import Any
from ofnodes.nodes.singlynode import SinglyNode
from ofnodes.structures.singlylinkedlist import SinglyLinkedList

NODES: dict[str, Any] = {
    "singly_node": SinglyNode("a pytest fixture"),
    "without_type_sized": {
        "none": SinglyNode(None),
        "int": SinglyNode(42),
        "float": SinglyNode(42.0),
        "bool": SinglyNode(True),
        "func": SinglyNode(lambda x: str(x)*2),  # pylint: disable=W0108
    },
    "with_type_sized": {
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
    },
}


@pytest.fixture
def example_singly_node() -> dict[str, SinglyNode]:
    return {
        'example_node_1': NODES["singly_node"],
        'example_node_2': NODES["without_type_sized"]["int"],
        'empty_node': NODES["without_type_sized"]["none"]
    }


@pytest.fixture
def example_singly_node_without_type_sized() -> dict[str, Any]:
    """Notice the values used in this fixture compared
    to the fixture `example_singly_node_type_sized`.

    ofnodes.structures.singlylinkedlist supports built in types
    and singlynode.SinglyNode type.
    """
    return NODES['without_type_sized']


@pytest.fixture
def example_singly_node_type_sized() -> dict[str, SinglyNode]:
    """The SinglyLinkedNode __str__() displays a message
    depending on the data it holds.
    The type hints will warn you about calling `len()`
    on a type that could lack `__len__`.
    Below are Singly Linked Nodes with data having __len__.
    """

    return {
        key: SinglyNode(value)
        for key, value in
        NODES['with_type_sized'].items()
        }


@pytest.fixture
def example_singly_linked_list() -> dict[str, SinglyLinkedList]:
    nodex: dict[str, SinglyNode] = {
        **NODES["with_type_sized"],
        **NODES["without_type_sized"],
    }

    sllist = SinglyLinkedList()
    list(sllist.insert_tail(node) for node in nodex.values())
    onenodesllist = SinglyLinkedList()
    onenodesllist.insert_tail(NODES['singly_node'])
    empty = SinglyLinkedList()
    return {
        "empty": empty,
        "one": onenodesllist,
        "example": sllist,
    }
