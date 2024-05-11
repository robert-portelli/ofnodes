import pytest
from ofnodes.structures.singlylinkedlist import SinglyLinkedList

class TestRemoveMixin:
    def test_remove_head(self):
        def test_empty_list():
            sllist = SinglyLinkedList()
            with pytest.raises(ValueError) as exc_info:
                sllist.remove_head()
            assert "Cannot remove head from empty linked structure" in str(exc_info)
        def test_one_node_list():
            sllist = SinglyLinkedList([42])
            head = sllist.head
            removed = sllist.remove_tail()
            assert head is removed
            assert sllist.head is None
            assert sllist.tail is None
        def test_two_node_list():
            sllist = SinglyLinkedList(['foo', 'bar'])
            head = sllist.head
            removed = sllist.remove_head()
            assert head is removed
            assert sllist.tail is sllist.head
        def test_three_node_list():
            sllist = SinglyLinkedList(['foo', 'bar', 'baz'])
            head = sllist.head
            removed = sllist.remove_head()
            assert head is removed
            assert removed.next is sllist.head
            assert sllist.head.next is sllist.tail
            assert sllist.tail.next is None
        def test_remove_first_encounter():
            sllist = SinglyLinkedList(['foo', 'bar', 'bar'])
            first_encounter = sllist.head.next
            sllist.remove('bar')
            assert first_encounter is not sllist.tail
        test_empty_list()
        test_one_node_list()
        test_two_node_list()
        test_three_node_list()
        test_remove_first_encounter()

    def test_remove_tail(self):
        def test_empty_list():
            sllist = SinglyLinkedList()
            with pytest.raises(ValueError) as exc_info:
                sllist.remove_tail()
            assert "Cannot remove tail from empty list" in str(exc_info)
        def test_one_node_list():
            sllist = SinglyLinkedList([42])
            tail = sllist.tail
            removed = sllist.remove_tail()
            assert tail is removed
            assert sllist.head is None
            assert sllist.tail is None

        def test_two_node_list():
            sllist = SinglyLinkedList(['foo', 'bar'])
            tail = sllist.tail
            removed = sllist.remove_tail()
            assert tail is removed
            assert sllist.head is sllist.tail
            assert sllist.head.next is None
            assert sllist.tail.next is None

        def test_more_than_two_node_list():
            sllist = SinglyLinkedList(['foo', 'bar', 'baz'])
            tail = sllist.tail
            removed = sllist.remove_tail()
            assert tail is removed
            assert sllist.tail is sllist.head.next
            assert sllist.tail.next is None
        test_empty_list()
        test_one_node_list()
        test_two_node_list()
        test_more_than_two_node_list()

    def test_remove(self):
        def test_remove_head():
            sllist = SinglyLinkedList([42])
            head = sllist.head
            removed = sllist.remove(42)
            assert head is removed
        def test_remove_tail():
            sllist = SinglyLinkedList(['foo', 'bar', 'baz'])
            tail = sllist.tail
            removed = sllist.remove('baz')
            assert tail is removed
        def test_remove_between_head_and_tail():
            sllist = SinglyLinkedList(['foo', 'bar', 'baz'])
            node = sllist.head.next
            removed = sllist.remove('bar')
            assert node is removed
        test_remove_head()
        test_remove_tail()
        test_remove_between_head_and_tail()
