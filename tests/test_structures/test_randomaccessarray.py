import pytest
from ofnodes.structures.randomaccessarray import RandomAccessArray

class TestRandomAccessArray:


    class TestSortingInstanceMethods:


        def test_ascending_bubble_sort(self):
            raarray = RandomAccessArray(5)
            [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            raarray.bubble_sort()
            assert repr(raarray) == 'RandomAccessArray([2, 4, 5, 6, 8])'
            assert str(raarray) == '[2, 4, 5, 6, 8]'

        def test_descending_bubble_sort(self):
            raarray = RandomAccessArray(5)
            [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            raarray.bubble_sort(ascending=False)
            assert repr(raarray) == 'RandomAccessArray([8, 6, 5, 4, 2])'
            assert str(raarray) == '[8, 6, 5, 4, 2]'

        def test_ascending_insertion_sort(self):
            raarray = RandomAccessArray(5)
            [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            raarray.insertion_sort()
            assert repr(raarray) == 'RandomAccessArray([2, 4, 5, 6, 8])'
            assert str(raarray) == '[2, 4, 5, 6, 8]'

        def test_descending_insertion_sort(self):
            raarray = RandomAccessArray(5)
            for i, val in enumerate([8, 2, 6, 1, 5]):
                raarray[i] = val
            raarray.insertion_sort(ascending=False)
            assert repr(raarray) == 'RandomAccessArray([8, 6, 5, 2, 1])'

        def test_custom_key_insertion_sort_ascending(self):
            # Custom comparison function
            def by_length(s):
                return len(s)

            strings = ["strawberry", "peach", "cherry", "date",]
            raarray = RandomAccessArray(len(strings))

            for i, val in enumerate(strings):
                raarray[i] = val

            raarray.insertion_sort(key=by_length)
            assert repr(raarray) == "RandomAccessArray(['date', 'peach', 'cherry', 'strawberry'])"

        def test_custom_key_insertion_sort_descending(self):
            # Custom comparison function
            def by_length(s):
                return len(s)

            strings = ["strawberry", "peach", "cherry", "date",]
            raarray = RandomAccessArray(len(strings))

            for i, val in enumerate(strings):
                raarray[i] = val

            raarray.insertion_sort(ascending=False, key=by_length)
            assert repr(raarray) == "RandomAccessArray(['strawberry', 'cherry', 'peach', 'date'])"

        def test_reverse_order(self):
            raarray = RandomAccessArray(5)
            [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
            raarray.reverse_order()
            assert repr(raarray) == 'RandomAccessArray([5, 4, 6, 2, 8])'
            assert str(raarray) == '[5, 4, 6, 2, 8]'
