import pytest
from ofnodes.sorting.mixins import BubbleSortMixin, ReverseOrderMixin
from ofnodes.structures.singlylinkedlist import SinglyLinkedList
from ofnodes.structures.randomaccessarray import RandomAccessArray

class TestBubbleSortMixin:
    def test_reference_based_bubble_sort(self):
        sllist = SinglyLinkedList()
        with pytest.raises(ValueError) as exc_info:
            sllist.reference_based_bubble_sort()
        assert "empty linked list" in str(exc_info)
        def ascending():
            sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            sllist.reference_based_bubble_sort()
            assert repr(sllist) == 'SinglyLinkedList([2, 4, 5, 6, 8])'
            assert str(sllist) == '2 -> 4 -> 5 -> 6 -> 8'

        def descending():
            sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            sllist.reference_based_bubble_sort(ascending=False)
            assert repr(sllist) == 'SinglyLinkedList([8, 6, 5, 4, 2])'
            assert str(sllist) == '8 -> 6 -> 5 -> 4 -> 2'

        ascending()
        descending()

    def test_index_based_bubble_sort(self):
        pass