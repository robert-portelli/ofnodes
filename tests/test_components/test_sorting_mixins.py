import pytest
#from ofnodes.sorting.mixins import BubbleSortMixin, ReverseOrderMixin
from ofnodes.structures.singlylinkedlist import SinglyLinkedList
from ofnodes.structures.randomaccessarray import RandomAccessArray

class TestBubbleSortMixin:
    def test_reference_based_bubble_sort(self):
        def test_no_head():
            raarray = RandomAccessArray(5)
            with pytest.raises(TypeError) as exc_info:
                raarray.reference_based_bubble_sort()
            assert "reference_based_bubble_sort" in str(exc_info)
        def test_empty_list():
            sllist = SinglyLinkedList()
            sllist.reference_based_bubble_sort()
        def test_one_node():
            sllist = SinglyLinkedList([42])
            sllist.reference_based_bubble_sort()
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
        test_one_node()
        test_ascending()
        test_descending()

    def test_index_based_bubble_sort(self):
        def test_no__getitem__():
            sllist = SinglyLinkedList()
            with pytest.raises(TypeError) as exc_info:
                sllist.index_based_bubble_sort()
            assert "index_based_bubble_sort" in str(exc_info)
        def test_empty_data_structure():
            raarray = RandomAccessArray(0)
            raarray.index_based_bubble_sort()
        def test_single_element():
            raarray = RandomAccessArray(1)
            raarray[0] = 1
            raarray.index_based_bubble_sort()
            assert raarray[0] == 1
        def test_already_sorted():
            raarray = RandomAccessArray(5)
            for i, val in enumerate([1, 2, 3, 4, 5]):
                raarray[i] = val
            raarray.index_based_bubble_sort()
            assert raarray._data == [1, 2, 3, 4, 5]
        def test_reverse_sorted():
            raarray = RandomAccessArray(5)
            for i, val in enumerate([5, 4, 3, 2, 1]):
                raarray[i] = val
            raarray.index_based_bubble_sort()
            assert raarray._data == [1, 2, 3, 4, 5]
        def test_all_elements_same():
            raarray = RandomAccessArray(5)
            for i in range(5):
                raarray[i] = 1
            raarray.index_based_bubble_sort()
            assert raarray._data == [1, 1, 1, 1, 1]
        def test_sort_ascending():
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
        @pytest.mark.performance
        def test_large_data_structure():
            import random
            raarray = RandomAccessArray(10000)
            random_values = random.sample(range(10000), 10000)
            for i, val in enumerate(random_values):
                raarray[i] = val
            raarray.index_based_bubble_sort()
            assert raarray._data == sorted(random_values)

        test_no__getitem__()
        test_empty_data_structure()
        test_single_element()
        test_already_sorted()
        test_reverse_sorted()
        test_all_elements_same()
        test_sort_ascending()
        test_descending()
        test_large_data_structure()

class TestInsertionSortMixin:
    def test_reference_based_insertion_sort(self):
        def test_no_head():
            raarray = RandomAccessArray(5)
            with pytest.raises(TypeError) as exc_info:
                raarray.reference_based_insertion_sort()
            assert "reference-based" in str(exc_info)
        def test_empty_list():
            sllist = SinglyLinkedList()
            with pytest.raises(ValueError) as exc_info:
                sllist.reference_based_insertion_sort()
            assert "Cannot sort an empty or one node linked list" in str(exc_info)
        def test_logic():
            sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([2, 4, 5, 6, 8])'
            assert str(sllist) == '2 -> 4 -> 5 -> 6 -> 8'
        def test_partial_sorted_list():
            sllist = SinglyLinkedList([2, 4, 3, 1, 5])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([1, 2, 3, 4, 5])'
            assert str(sllist) == '1 -> 2 -> 3 -> 4 -> 5'
        def test_sorted_list():
            sllist = SinglyLinkedList([1, 2, 3, 4, 5])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([1, 2, 3, 4, 5])'
            assert str(sllist) == '1 -> 2 -> 3 -> 4 -> 5'
        def test_unsorted_list():
            sllist = SinglyLinkedList([5, 2, 7, 1, 9])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([1, 2, 5, 7, 9])'
            assert str(sllist) == '1 -> 2 -> 5 -> 7 -> 9'
        def test_one_node_list():
            sllist = SinglyLinkedList([42])
            with pytest.raises(ValueError) as exc_info:
                sllist.reference_based_insertion_sort()
            assert "Cannot sort an empty or one node linked list" in str(exc_info)
        def test_sorted_two_node_list():
            sllist = SinglyLinkedList([2, 4])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([2, 4])'
            assert str(sllist) == '2 -> 4'
        def test_unsorted_two_node_list():
            sllist = SinglyLinkedList([4, 2])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([2, 4])'
            assert str(sllist) == '2 -> 4'
        def test_two_same_node_list():
            sllist = SinglyLinkedList([2, 2])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([2, 2])'
            assert str(sllist) == '2 -> 2'
        test_no_head()
        test_empty_list()
        test_logic()
        test_partial_sorted_list()
        test_sorted_list()
        test_unsorted_list()
        test_one_node_list()
        test_sorted_two_node_list()
        test_unsorted_two_node_list()
        test_two_same_node_list()
    def test_index_based_insertion_sort(self):
        def test_error():
            sllist = SinglyLinkedList()
            with pytest.raises(TypeError) as exc_info:
                sllist.index_based_insertion_sort()
            assert "index_based_insertion_sort" in str(exc_info)
        def test_logic():
            raarray = RandomAccessArray(5)
            [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            raarray.index_based_insertion_sort()
            assert repr(raarray) == 'RandomAccessArray([2, 4, 5, 6, 8])'
            assert str(raarray) == '[2, 4, 5, 6, 8]'
        test_error()
        test_logic()

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