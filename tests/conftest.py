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

@pytest.fixture
def easy_singly_linked_list() -> SinglyLinkedList:
    llist = SinglyLinkedList()
    for i in range(1, 4):
        llist.tail = f"{i} node"
    # [setattr(llist, 'tail', f"{i} node") for i in range(3)]

    return llist