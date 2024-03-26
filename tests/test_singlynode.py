def test_init(example_singly_node):
    assert example_singly_node.data == "a pytest fixture"


def test_repr(example_singly_node):
    assert repr(example_singly_node) == "SinglyNode(data='a pytest fixture')"



def test__str__with_not_type_sized(example_singly_node_without_type_sized):
    assert (
        str(example_singly_node_without_type_sized['none'])
        == "This node's data is of type <class 'NoneType'>"
        and
        str(example_singly_node_without_type_sized['int'])
        == "This node's data is of type <class 'int'>"
        and
        str(example_singly_node_without_type_sized['float'])
        == "This node's data is of type <class 'float'>"
        and
        str(example_singly_node_without_type_sized['bool'])
        == "This node's data is of type <class 'bool'>"
        and
        str(example_singly_node_without_type_sized['func'])
        == "This node's data is of type <class 'function'>"
    )

def test__str__with_type_sized(example_singly_node_type_sized):
    assert (
        str(example_singly_node_type_sized['list'])
        == "This node's data is 4 of type <class 'list'>."
        and
        str(example_singly_node_type_sized['dict'])
        == "This node's data is 2 of type <class 'dict'>."
        and
        str(example_singly_node_type_sized['string'])
        == "This node's data is 13 of type <class 'str'>."
        and
        str(example_singly_node_type_sized['set'])
        == "This node's data is 5 of type <class 'set'>."
        and
        str(example_singly_node_type_sized['bytes'])
        == "This node's data is 3 of type <class 'bytes'>."
        and
        str(example_singly_node_type_sized['bytearray'])
        == "This node's data is 4 of type <class 'bytearray'>."
        and
        str(example_singly_node_type_sized['range'])
        == "This node's data is 43 of type <class 'range'>."
    )
