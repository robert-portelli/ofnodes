import pytest
from ofnodes.structures.randomaccessarray import RandomAccessArray
#from ofnodes.structures.singlylinkedlist import SinglyLinkedList

def test_bubble_sort():
    def test_ascending():
        raarray = RandomAccessArray(5)
        [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
        raarray.bubble_sort()
        assert repr(raarray) == 'RandomAccessArray([2, 4, 5, 6, 8])'
        assert str(raarray) == '[2, 4, 5, 6, 8]'
    def test_descending():
        raarray = RandomAccessArray(5)
        [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
        raarray.bubble_sort(ascending=False)
        assert repr(raarray) == 'RandomAccessArray([8, 6, 5, 4, 2])'
        assert str(raarray) == '[8, 6, 5, 4, 2]'
    test_ascending()
    test_descending()

def test_reverse_order():
    raarray = RandomAccessArray(5)
    [raarray.__setitem__(i, val) for i, val in enumerate([8, 2, 6, 4, 5])]
    raarray.reverse_order()
    assert repr(raarray) == 'RandomAccessArray([5, 4, 6, 2, 8])'
    assert str(raarray) == '[5, 4, 6, 2, 8]'
