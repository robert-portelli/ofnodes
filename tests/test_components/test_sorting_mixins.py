import pytest
#from ofnodes.sorting.mixins import BubbleSortMixin, ReverseOrderMixin
from ofnodes.structures.singlylinkedlist import SinglyLinkedList
from ofnodes.structures.randomaccessarray import RandomAccessArray

class TestBubbleSortMixin():
    def test_reference_based_bubble_sort(self):
        def test_no_head():
            raarray = RandomAccessArray(5)
            with pytest.raises(TypeError) as exc_info:
                raarray.reference_based_bubble_sort()
            assert "reference_based_bubble_sort" in str(exc_info)
        def test_empty_list():
            sllist = SinglyLinkedList()
            with pytest.raises(ValueError) as exc_info:
                sllist.reference_based_bubble_sort()
            assert "empty linked list" in str(exc_info)
        def test_ascending():
            sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            sllist.reference_based_bubble_sort()
            assert repr(sllist) == 'SinglyLinkedList([2, 4, 5, 6, 8])'
            assert str(sllist) == '2 -> 4 -> 5 -> 6 -> 8'

        def test_descending():
            sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            sllist.reference_based_bubble_sort(ascending=False)
            assert repr(sllist) == 'SinglyLinkedList([8, 6, 5, 4, 2])'
            assert str(sllist) == '8 -> 6 -> 5 -> 4 -> 2'
        test_no_head()
        test_empty_list()
        test_ascending()
        test_descending()

    def test_index_based_bubble_sort(self):
        def test_no__getitem__():
            sllist = SinglyLinkedList()
            with pytest.raises(TypeError) as exc_info:
                sllist.index_based_bubble_sort()
            assert "index_based_bubble_sort" in str(exc_info)
        def test_empty_array():
            raarray = RandomAccessArray(5)
            with pytest.raises(TypeError) as exc_info:
                raarray.index_based_bubble_sort()
            assert "'NoneType' and 'NoneType'" in str(exc_info)
        def test_ascending():
            raarray = RandomAccessArray(5)
            [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            raarray.index_based_bubble_sort()
            assert repr(raarray) == 'RandomAccessArray([2, 4, 5, 6, 8])'
            assert str(raarray) == '[2, 4, 5, 6, 8]'
        def test_descending():
            raarray = RandomAccessArray(5)
            [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            raarray.index_based_bubble_sort(ascending=False)
            assert repr(raarray) == 'RandomAccessArray([8, 6, 5, 4, 2])'
            assert str(raarray) == '[8, 6, 5, 4, 2]'
        test_no__getitem__()
        test_empty_array()
        test_ascending()
        test_descending()

    class TestReverseOrderMixin:
        def test_reference_based_reverse_order(self):
            def test_no_head():
                raarray = RandomAccessArray(5)
                with pytest.raises(TypeError) as exc_info:
                    raarray.reference_based_reverse_order()
                assert "reference_based_reverse_order" in str(exc_info)
            def test_empty_list():
                sllist = SinglyLinkedList()
                with pytest.raises(ValueError) as exc_info:
                    sllist.reference_based_reverse_order()
                assert "empty linked list" in str(exc_info)

            def test_reverse_order():
                sllist = SinglyLinkedList([8, 2, 6, 4, 5])
                sllist.reference_based_reverse_order()
                assert repr(sllist) == 'SinglyLinkedList([5, 4, 6, 2, 8])'
                assert str(sllist) == '5 -> 4 -> 6 -> 2 -> 8'

            test_no_head()
            test_empty_list()
            test_reverse_order()

        def test_index_based_reverse_order(self):
            def test_no__getitem__():
                sllist = SinglyLinkedList()
                with pytest.raises(TypeError) as exc_info:
                    sllist.index_based_reverse_order()
                assert "index_based_reverse_order" in str(exc_info)
            #def test_empty_array():
            #    # TODO: shouldn't reverse an array[i] is None
            #    raarray = RandomAccessArray(5)
            #    with pytest.raises(TypeError) as exc_info:
            #        raarray.index_based_reverse_order()
            #    assert "'NoneType' and 'NoneType'" in str(exc_info)
            def test_reverse_order():
                raarray = RandomAccessArray(5)
                [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
                raarray.index_based_reverse_order()
                assert repr(raarray) == 'RandomAccessArray([5, 4, 6, 2, 8])'
                assert str(raarray) == '[5, 4, 6, 2, 8]'
            test_no__getitem__()
            #test_empty_array()
            test_reverse_order()