import pytest

from ofnodes.nodes.singlynode import SinglyNode

@pytest.fixture
def example_singly_node():
    return SinglyNode("a pytest fixture")

@pytest.fixture
def example_singly_node_without_type_sized():
    return {
        'none': SinglyNode(None),
        'int': SinglyNode(42),
        'float': SinglyNode(42.0),
        'bool': SinglyNode(True),
        'func': SinglyNode(lambda x: str(x)) # pylint: disable=W0108
    }

@pytest.fixture
def example_singly_node_type_sized():
    examples = {
        'list': ['cat', 42, 42.0, True,],
        'dict': {0: 'one', 1: ('tuple', 'dog'),},
        'string': '13 characters',
        'set': {'one', 2, 3.0, False, None,},
        'bytes': bytes([65, 66, 67,]),
        'bytearray': bytearray(b'LGRW'),
        'range': range(0, 43),
    }
    return {
        key: SinglyNode(value) for key,value in examples.items()
    }
