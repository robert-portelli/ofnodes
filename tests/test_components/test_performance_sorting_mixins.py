import pytest
from ofnodes.structures.randomaccessarray import RandomAccessArray
from ofnodes.structures.singlylinkedlist import SinglyLinkedList

class TestPerformanceReferenceBasedBubbleSort:
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

class TestPerformanceReferenceBasedInsertionSort:
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