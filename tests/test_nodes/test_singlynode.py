def test_init(example_singly_node):
    assert (
        example_singly_node.data == "a pytest fixture"
        and
        example_singly_node.next is None
    )


def test__repr__(example_singly_node):
    assert (
        repr(example_singly_node)
        ==
        "SinglyNode(data='a pytest fixture')"
    )



def test__str__with_not_type_sized(example_singly_node_without_type_sized):
    assert (
        str(example_singly_node_without_type_sized['none'])
        == "This node's data is of type NoneType."
        and
        str(example_singly_node_without_type_sized['int'])
        == "This node's data is of type int."
        and
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

def test_argument_assignment(example_singly_node):
    """Test if the data argument can be assigned.
    """
    next_node = example_singly_node
    assert example_singly_node.data == 'a pytest fixture'
    example_singly_node.data = "a new string"
    assert example_singly_node.data == 'a new string'
    example_singly_node.next = next_node
