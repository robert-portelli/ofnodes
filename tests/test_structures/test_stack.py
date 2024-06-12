# tests/test_structures/test_stack.py
import pytest
from ofnodes.structures.stack import Stack

class TestStack:

    def test_dynamic_attribute_assignment(self):
        stack = Stack()
        with pytest.raises(AttributeError) as exc_info:
            stack.fail = True  # pylint: disable=assigning-non-slot
        assert "object has no attribute" in str(exc_info)