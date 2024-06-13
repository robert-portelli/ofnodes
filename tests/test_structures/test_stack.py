# tests/test_structures/test_stack.py
import pytest
from ofnodes.structures.stack import Stack
from ofnodes.nodes.singlynode import SinglyNode

class TestStack:

    def test_dynamic_attribute_assignment(self):
        stack = Stack()
        with pytest.raises(AttributeError) as exc_info:
            stack.fail = True  # pylint: disable=assigning-non-slot
        assert "object has no attribute" in str(exc_info)
    
    def test__init___values(self):
        stack = Stack([8, 2, 1, 5])
        assert repr(stack) == 'Stack([5, 1, 2, 8])'

    def test__dir__(self):
        stack = Stack()
        dirr = [
            '__class__',
            '__delattr__',
            '__dir__',
            '__doc__',
            '__eq__',
            '__format__',
            '__ge__',
            '__getattribute__',
            '__getstate__',
            '__gt__',
            '__hash__',
            '__init__',
            '__init_subclass__',
            '__le__',
            '__lt__',
            '__module__',
            '__ne__',
            '__new__',
            '__reduce__',
            '__reduce_ex__',
            '__repr__',
            '__setattr__',
            '__sizeof__',
            '__slots__',
            '__str__',
            '__subclasshook__',
            'display',
            'head',
            'is_empty',
            'peek',
            'pop',
            'print_node_data',
            'push',
            'remove',
            'remove_head',
            'remove_tail',
        ]
        assert dir(stack) == dirr
        assert "__dict__" not in str(dir(stack))

class Test__repr__and__str__:
    def test_empty_stack(self):
        stack = Stack()
        assert repr(stack) == 'Stack()'
        assert str(stack) == 'Empty Stack'

    def test_stack(self):
        stack = Stack([42, 'omaha', False])
        assert repr(stack) == "Stack([False, 'omaha', 42])"
        assert str(stack) == "False -> omaha -> 42"


class TestPush:
    stack = Stack()
    stack.push(42)
    assert repr(stack) == 'Stack([42])'
    assert str(stack) == '42'
    stack.push('foo')
    assert repr(stack) == "Stack(['foo', 42])"
    assert str(stack) == 'foo -> 42'

class TestPop:
    stack = Stack()
    with pytest.raises(ValueError) as exc_info:
        stack.pop()
    assert "empty linked structure" in str(exc_info)
    stack = Stack([4, 2])
    popped = stack.pop()
    assert isinstance(popped, SinglyNode)
    assert popped.data == 2
    popped = stack.pop()
    assert popped.data == 4
    assert stack._head is None

class TestPeek:
    stack = Stack([4, 2])
    assert stack.peek() == 2
    stack.pop()
    assert stack.peek() == 4
    stack.pop()
    with pytest.raises(IndexError) as exc_info:
        stack.peek()
    assert "Stack is empty" in str(exc_info)

class TestDisplay:
    def test_node_data_display(self, capsys):
        stack = Stack([2, 4])
        stack.display()
        captured = capsys.readouterr()
        expected_output = "4\n2\n"
        assert captured.out == expected_output

class TestIsEmpty:
    stack = Stack([42])
    assert not stack.is_empty()
    stack.pop()
    assert stack.is_empty()
