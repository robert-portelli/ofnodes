import pytest
from ofnodes.sorting.mixins import BubbleSortMixin, InsertionSortMixin
from ofnodes.structures.singlylinkedlist import SinglyLinkedList
from ofnodes.structures.randomaccessarray import RandomAccessArray

class TestBubbleSortMixin:


    class TestReferenceBasedBubbleSort:
        def test_no_head(self):
            class Dummy(BubbleSortMixin):
                pass
            dummy = Dummy()
            with pytest.raises(TypeError) as exc_info:
                dummy.reference_based_bubble_sort()
            assert "reference_based_bubble_sort" in str(exc_info)
        def test_not_comparable(self):
            class Dummy:
                pass
            sllist = SinglyLinkedList([Dummy(), Dummy()])
            with pytest.raises(TypeError) as exc_info:
                sllist.bubble_sort()
            assert "'>' not supported" in str(exc_info)
            with pytest.raises(TypeError) as exc_info:
                sllist.bubble_sort(ascending=False)
            assert "'<' not supported" in str(exc_info)
        def test_not_homogenous(self):
            sllist = SinglyLinkedList([42, "omaha"])
            with pytest.raises(TypeError) as exc_info:
                sllist.bubble_sort()
            assert "must be of the same type" in str(exc_info)
        def test_zero_nodes(self):
            sllist = SinglyLinkedList()
            sllist.reference_based_bubble_sort()
            assert repr(sllist) == 'SinglyLinkedList()'
        def test_one_node(self):
            sllist = SinglyLinkedList([42])
            sllist.reference_based_bubble_sort()
            assert repr(sllist) == 'SinglyLinkedList([42])'
        def test_two_nodes(self):
            sllist = SinglyLinkedList([4, 2])
            sllist.reference_based_bubble_sort()
            assert repr(sllist) == 'SinglyLinkedList([2, 4])'
        def test_already_sorted(self):
            sllist = SinglyLinkedList([1, 2, 3, 4, 5])
            sllist.reference_based_bubble_sort()
            assert repr(sllist) == 'SinglyLinkedList([1, 2, 3, 4, 5])'
        def test_reverse_sorted(self):
            sllist = SinglyLinkedList([5, 4, 3, 2, 1])
            sllist.reference_based_bubble_sort()
            assert repr(sllist) == 'SinglyLinkedList([1, 2, 3, 4, 5])'
        def test_all_elements_the_same(self):
            sllist = SinglyLinkedList([7, 7, 7])
            sllist.reference_based_bubble_sort()
            assert repr(sllist) == 'SinglyLinkedList([7, 7, 7])'
        def test_sort_ascending(self):
            sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            sllist.reference_based_bubble_sort()
            assert repr(sllist) == 'SinglyLinkedList([2, 4, 5, 6, 8])'
            assert str(sllist) == '2 -> 4 -> 5 -> 6 -> 8'
        def test_sort_descending(self):
            sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            sllist.reference_based_bubble_sort(ascending=False)
            assert repr(sllist) == 'SinglyLinkedList([8, 6, 5, 4, 2])'
            assert str(sllist) == '8 -> 6 -> 5 -> 4 -> 2'
        @pytest.mark.performance
        def test_large_data_structure(self):
            import random
            random_values = random.sample(range(10000), 10000)
            sllist = SinglyLinkedList(random_values)
            sllist.reference_based_bubble_sort()
            _ = sorted(random_values)
            current = sllist.head
            index = 0
            while current:
                assert current.data == _[index]
                current = current.next
                index += 1
        @pytest.mark.performance
        def test_large_data_structure_descending(self):
            import random
            random_values = random.sample(range(10000), 10000)
            sllist = SinglyLinkedList(random_values)
            sllist.reference_based_bubble_sort(ascending=False)
            _ = sorted(random_values, reverse=True)
            current = sllist.head
            index = 0
            while current:
                assert current.data == _[index]
                current = current.next
                index += 1
    class TestIndexBasedBubbleSort:

        def test_no__getitem__(self):
            class Dummy(BubbleSortMixin):
                pass

            dummy = Dummy()
            with pytest.raises(TypeError) as exc_info:
                dummy.index_based_bubble_sort()
            assert "only be used on data structures that support index-based access" in str(exc_info)
        def test_not_comparable(self):
            class Dummy:
                pass
            raarray = RandomAccessArray(5)
            for i in range(len(raarray)):  # pylint: disable=consider-using-enumerate
                raarray[i] = Dummy()
            with pytest.raises(TypeError) as exc_info:
                raarray.index_based_bubble_sort()
            assert "'>' not supported" in str(exc_info.value)
            with pytest.raises(TypeError) as exc_info:
                raarray.index_based_bubble_sort(ascending=False)
            assert "'<' not supported" in str(exc_info.value)

        def test_homogenous_elements(self):
            raarray = RandomAccessArray(2)
            raarray[0], raarray[1] = 42, 'hut'
            with pytest.raises(TypeError) as exc_info:
                raarray.index_based_bubble_sort()
            assert "must be of the same type" in str(exc_info)
        def test_empty_data_structure(self):
            raarray = RandomAccessArray(0)
            raarray.index_based_bubble_sort()
        def test_single_element(self):
            raarray = RandomAccessArray(1)
            raarray[0] = 1
            raarray.index_based_bubble_sort()
            assert raarray[0] == 1
        def test_already_sorted(self):
            raarray = RandomAccessArray(5)
            for i, val in enumerate([1, 2, 3, 4, 5]):
                raarray[i] = val
            raarray.index_based_bubble_sort()
            assert raarray._data == [1, 2, 3, 4, 5]
        def test_reverse_sorted(self):
            raarray = RandomAccessArray(5)
            for i, val in enumerate([5, 4, 3, 2, 1]):
                raarray[i] = val
            raarray.index_based_bubble_sort()
            assert raarray._data == [1, 2, 3, 4, 5]
        def test_all_elements_same(self):
            raarray = RandomAccessArray(5)
            for i in range(5):
                raarray[i] = 1
            raarray.index_based_bubble_sort()
            assert raarray._data == [1, 1, 1, 1, 1]
        def test_sort_ascending(self):
            raarray = RandomAccessArray(5)
            [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            raarray.index_based_bubble_sort()
            assert repr(raarray) == 'RandomAccessArray([2, 4, 5, 6, 8])'
            assert str(raarray) == '[2, 4, 5, 6, 8]'
        def test_descending(self):
            raarray = RandomAccessArray(5)
            [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            raarray.index_based_bubble_sort(ascending=False)
            assert repr(raarray) == 'RandomAccessArray([8, 6, 5, 4, 2])'
            assert str(raarray) == '[8, 6, 5, 4, 2]'
        @pytest.mark.performance
        def test_large_data_structure(self):  # pragma: no cover
            import random
            raarray = RandomAccessArray(10000)
            random_values = random.sample(range(10000), 10000)
            for i, val in enumerate(random_values):
                raarray[i] = val
            raarray.index_based_bubble_sort()
            assert raarray._data == sorted(random_values)
        @pytest.mark.performance
        def test_large_data_structure_descending(self):  # pragma: no cover
            import random
            raarray = RandomAccessArray(10000)
            random_values = random.sample(range(10000), 10000)
            for i, val in enumerate(random_values):
                raarray[i] = val
            raarray.index_based_bubble_sort(ascending=False)
            assert raarray._data == sorted(random_values, reverse=True)

class TestInsertionSortMixin:


    class TestReferenceBasedInsertionSortMixin:


        def test_wrong_object_type(self):
            class Dummy(InsertionSortMixin):
                pass
            dummy = Dummy()
            with pytest.raises(TypeError) as exc_info:
                dummy.reference_based_insertion_sort()
            assert "reference-based" in str(exc_info)
        def test_empty_list(self):
            sllist = SinglyLinkedList()
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList()'
        def test_heterogenous(self):
            sllist = SinglyLinkedList([42.0, True])
            with pytest.raises(TypeError) as exc_info:
                sllist.reference_based_insertion_sort()
            assert "must be of the same type" in str(exc_info)
        def test_logic(self):
            sllist = SinglyLinkedList([8, 2, 6, 4, 5])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([2, 4, 5, 6, 8])'
            assert str(sllist) == '2 -> 4 -> 5 -> 6 -> 8'
        def test_partial_sorted_list(self):
            sllist = SinglyLinkedList([2, 4, 3, 1, 5])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([1, 2, 3, 4, 5])'
            assert str(sllist) == '1 -> 2 -> 3 -> 4 -> 5'
        def test_sorted_list(self):
            sllist = SinglyLinkedList([1, 2, 3, 4, 5])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([1, 2, 3, 4, 5])'
            assert str(sllist) == '1 -> 2 -> 3 -> 4 -> 5'
        def test_unsorted_list(self):
            sllist = SinglyLinkedList([5, 2, 7, 1, 9])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([1, 2, 5, 7, 9])'
            assert str(sllist) == '1 -> 2 -> 5 -> 7 -> 9'
        def test_one_node_list(self):
            sllist = SinglyLinkedList([42])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([42])'
        def test_sorted_two_node_list(self):
            sllist = SinglyLinkedList([2, 4])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([2, 4])'
            assert str(sllist) == '2 -> 4'
        def test_unsorted_two_node_list(self):
            sllist = SinglyLinkedList([4, 2])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([2, 4])'
            assert str(sllist) == '2 -> 4'
        def test_two_same_node_list(self):
            sllist = SinglyLinkedList([2, 2])
            sllist.reference_based_insertion_sort()
            assert repr(sllist) == 'SinglyLinkedList([2, 2])'
            assert str(sllist) == '2 -> 2'
        def test_descending_one_node_list(self):
            sllist = SinglyLinkedList([42])
            sllist.reference_based_insertion_sort(ascending=False)
            assert repr(sllist) == 'SinglyLinkedList([42])'
        def test_descending_sorted_two_node_list(self):
            sllist = SinglyLinkedList([2, 4])
            sllist.reference_based_insertion_sort(ascending=False)
            assert repr(sllist) == 'SinglyLinkedList([4, 2])'
            assert str(sllist) == '4 -> 2'
        def test_descending_unsorted_list(self):
            sllist = SinglyLinkedList([5, 2, 7, 1, 9])
            sllist.reference_based_insertion_sort(ascending=False)
            assert repr(sllist) == 'SinglyLinkedList([9, 7, 5, 2, 1])'
            assert str(sllist) == '9 -> 7 -> 5 -> 2 -> 1'
        def test_descending_sorted_list(self):
            sllist = SinglyLinkedList([5, 4, 3, 2, 1])
            sllist.reference_based_insertion_sort(ascending=False)
            assert repr(sllist) == 'SinglyLinkedList([5, 4, 3, 2, 1])'
            assert str(sllist) == '5 -> 4 -> 3 -> 2 -> 1'
        def test_ascending_value_error(self):
            sllist = SinglyLinkedList([5, 4, 3, 2, 1])
            with pytest.raises(ValueError) as exc_info:
                sllist.reference_based_insertion_sort(ascending='omaha')
            assert "Unexpected value" in str(exc_info)
        def test_descending_two_same_node_list(self):
            sllist = SinglyLinkedList([2, 2])
            sllist.reference_based_insertion_sort(ascending=False)
            assert repr(sllist) == 'SinglyLinkedList([2, 2])'
            assert str(sllist) == '2 -> 2'

        def test_custom_key_ascending(self):
            def by_length(s):
                return len(s)
            fruits = ['cherry', 'strawberry', 'fig', 'peach', ]
            sllist = SinglyLinkedList(fruits)
            tims = sorted(fruits, key=by_length)
            sllist.reference_based_insertion_sort(key=by_length)
            current = sllist._head
            index = 0
            while current:
                assert current._data == tims[index]
                current = current._next
                index += 1

        def test_custom_key_descending(self):
            def by_length(s):
                return len(s)
            fruits = ['cherry', 'strawberry', 'fig', 'peach', ]
            sllist = SinglyLinkedList(fruits)
            tims = sorted(fruits, key=by_length, reverse=True)
            sllist.reference_based_insertion_sort(ascending=False, key=by_length)
            current = sllist._head
            index = 0
            while current:
                assert current._data == tims[index]
                current = current._next
                index += 1

        @pytest.mark.performance
        def test_large_data_structure(self):
            import random
            random_values = random.sample(range(10000), 10000)
            sllist = SinglyLinkedList(random_values)
            sllist.reference_based_insertion_sort()
            _ = sorted(random_values)
            current = sllist._head
            index = 0
            while current:
                assert current._data == _[index]
                current = current._next
                index += 1
        @pytest.mark.performance
        def test_large_data_structure_descending(self):
            import random
            random_values = random.sample(range(10000), 10000)
            sllist = SinglyLinkedList(random_values)
            sllist.reference_based_insertion_sort(ascending=False)
            _ = sorted(random_values, reverse=True)
            current = sllist.head
            index = 0
            while current:
                assert current.data == _[index]
                current = current.next
                index += 1


    class TestIndexBasedInsertionSortMixin:
        def test_wrong_object_type(self):
            class Dummy(InsertionSortMixin):
                pass
            dummy = Dummy()
            with pytest.raises(TypeError) as exc_info:
                dummy.index_based_insertion_sort()
            assert "index_based_insertion_sort" in str(exc_info)
        def test_logic(self):
            raarray = RandomAccessArray(5)
            [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            raarray.index_based_insertion_sort()
            assert repr(raarray) == 'RandomAccessArray([2, 4, 5, 6, 8])'
            assert str(raarray) == '[2, 4, 5, 6, 8]'
        def test_zero_elements(self):
            raarray = RandomAccessArray(0)
            raarray.index_based_insertion_sort()
            assert repr(raarray) == 'RandomAccessArray([])'
        def test_one_element(self):
            raarray = RandomAccessArray(1)
            raarray[0] = 42
            raarray.index_based_insertion_sort()
            assert repr(raarray) == 'RandomAccessArray([42])'

        def test_custom_comparison_function(self):
            strings = ["apple", "banana", "cherry", "date"]

            # Custom comparison function
            def by_length(s):
                return len(s)

            # Using the custom comparison function with insertion sort
            raarray = RandomAccessArray(len(strings))
            for i, val in enumerate(strings):
                raarray[i] = val

            assert repr(raarray) == "RandomAccessArray(['apple', 'banana', 'cherry', 'date'])"
            raarray.index_based_insertion_sort(key=by_length)
            assert repr(raarray) == "RandomAccessArray(['date', 'apple', 'banana', 'cherry'])"
        def test_descending_sort(self):
            raarray = RandomAccessArray(5)
            for i, val in enumerate([8, 2, 6, 1, 5]):
                raarray[i] = val
            raarray.index_based_insertion_sort(ascending=False)
            assert repr(raarray) == 'RandomAccessArray([8, 6, 5, 2, 1])'


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