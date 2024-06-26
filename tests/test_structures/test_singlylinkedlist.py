import pytest
from ofnodes.structures.singlylinkedlist import SinglyLinkedList
from ofnodes.nodes.singlynode import SinglyNode

class TestCycleDetectionMixin:
    """The test class for cycle detection in reference-based structures."""
    def test_cycle_discouragement(self):
        sllist = SinglyLinkedList([8, 2, 6, 4, 5])
        # the ofnodes library doesn't create tail cycles
        assert sllist.tail.next is None
        assert sllist.cycle_detection() is False
        # the ofnodes library discourages cycle creation
        with pytest.raises(AttributeError) as exc_info:
            sllist.tail.next = sllist.head
        assert "Cannot set 'next' attribute directly." in str(exc_info)
    def test_tail_cycle_detection(self):
        sllist = SinglyLinkedList([8, 2, 6, 4, 5])
        # bypass `SinglyNode.next` setter to create cycle
        setattr(sllist.tail, "_next", sllist.head.next)
        assert sllist.tail.next is not None
        assert sllist.cycle_detection() is True
    def test_not_tail_cycle(self):
        sllist = SinglyLinkedList([8, 2, 6, 4, 5])
        setattr(sllist.head, '_next', sllist.head)
        assert sllist.cycle_detection() is True
        sllist = SinglyLinkedList([8, 2, 6, 4, 5])
        setattr(sllist.head.next, '_next', sllist.head.next)
        assert sllist.cycle_detection() is True

class TestSinglyLinkedList:
    def test_dynamic_attribute_assignment(self):
        sllist = SinglyLinkedList()
        with pytest.raises(AttributeError) as exc_info:
            sllist.fail = True  # pylint: disable=assigning-non-slot
        assert "object has no attribute" in str(exc_info)


    def test__init__(self):
        sllist = SinglyLinkedList()
        assert sllist.head is None and sllist.tail is None and sllist.target is None
        sllist = SinglyLinkedList(["foo", 42.0, True])
        assert (
            getattr(sllist.head, "data") == "foo"
            and getattr(sllist.head.next, "data") == 42.0
            and getattr(sllist.tail, "data") is True
        )


    def test__add__(self):
        sllist = SinglyLinkedList()
        sllist + "foo"
        assert sllist.head.data == "foo"
        sllist + "bar"
        assert sllist.tail.data == "bar"


    def test__repr__(self):
        sllist = SinglyLinkedList()
        assert repr(sllist) == "SinglyLinkedList()"
        sllist = SinglyLinkedList(["foo", 42.0, True])
        assert repr(sllist) == "SinglyLinkedList(['foo', 42.0, True])"


    def test__str__(self):
        sllist = SinglyLinkedList()
        assert str(sllist) == "Empty Singly Linked List"
        sllist = SinglyLinkedList(["foo", 42.0, True])
        assert str(sllist) == "foo -> 42.0 -> True"


    def test__dir__(self):
        sllist = SinglyLinkedList()
        dirr = [
            "__add__",
            "__class__",
            "__delattr__",
            "__dir__",
            "__doc__",
            "__eq__",
            "__format__",
            "__ge__",
            "__getattribute__",
            "__getstate__",
            "__gt__",
            "__hash__",
            "__init__",
            "__init_subclass__",
            "__le__",
            "__lt__",
            "__module__",
            "__ne__",
            "__new__",
            "__reduce__",
            "__reduce_ex__",
            "__repr__",
            "__setattr__",
            "__sizeof__",
            "__slots__",
            "__str__",
            "__subclasshook__",
            "bubble_sort",
            "cycle_detection",
            "head",
            "insert_after_target",
            "insert_before_target",
            "insert_head",
            "insert_tail",
            "insertion_sort",
            "print_node_data",
            "reference_based_cycle_detection",
            "remove",
            "remove_head",
            "remove_tail",
            "reverse_order",
            "search",
            "tail",
            "target",
        ]
        assert dir(sllist) == dirr
        assert "__dict__" not in str(dir(sllist))

class TestHeadProperty:
    def test_head_setter_and_getter(self):
        sllist = SinglyLinkedList()
        assert sllist.head is None
        sllist.head = "a string"
        assert isinstance(sllist.head, SinglyNode)
        sllist.head = SinglyNode("b string")

    def test_head_deleter(self):
        sllist = SinglyLinkedList()
        with pytest.raises(AttributeError) as exc_info:
            del sllist.head

        assert "cannot be deleted" in str(exc_info.value)
    
    def test_insert_head(self):
        sllist = SinglyLinkedList()
        sllist.insert_head("string")
        assert sllist.head.data == "string"


class TestTailProperty:
    def test_tail_setter(self):
        sllist = SinglyLinkedList()
        assert sllist.head is None and sllist.tail is None
        node = SinglyNode("a string")
        tup = (42, ["this", True])
        sllist.tail = node
        assert sllist.head == node and sllist.tail == node and sllist.head is sllist.tail

        sllist.tail = tup  # trigger tail setter

        assert (
            sllist.head is not sllist.tail
            and sllist.head == node
            and isinstance(sllist.tail, SinglyNode)
            and sllist.tail.data == tup
        )


    def test_tail_deleter(self):
        sllist = SinglyLinkedList()
        with pytest.raises(AttributeError) as exc_info:
            del sllist.tail

        assert "cannot be deleted" in str(exc_info.value)

class TestSearch:
    def test_invalid_target(self):
        llist = SinglyLinkedList()
        with pytest.raises(ValueError) as exc_info:
            llist.target = "will error"
        assert "Cannot assign" in str(exc_info)

    def test_empty_list(self):
        llist = SinglyLinkedList()
        with pytest.raises(ValueError) as exc_info:
            llist.search("some target data")
        assert "Cannot search" in str(exc_info)

    def test_found_and_not_found(self):
        llist = SinglyLinkedList()
        list(llist.insert_tail(f"{i} node") for i in range(1, 5))
        assert llist.search("1 node") is True
        assert llist.search("42 node") is False



def test_print_node_data(capsys):
    sllist = SinglyLinkedList()
    list(sllist.insert_tail(f"{i} node") for i in range(1, 5))

    # Call the print_node_data method
    sllist.print_node_data()

    # Capture the printed output
    captured = capsys.readouterr()

    # Verify the printed output matches the expected output
    expected_output = "1 node\n2 node\n3 node\n4 node\n"
    assert captured.out == expected_output

class TestTarget:
    def test_empty_list(self):
        sllist = SinglyLinkedList()
        with pytest.raises(ValueError) as exc_info:
            sllist.target = "will error"
        assert "Cannot assign" in str(exc_info)

    def test_deleter(self):
        sllist = SinglyLinkedList()
        with pytest.raises(AttributeError) as exc_info:
            del sllist.target
        assert "cannot be deleted" in str(exc_info)

    def test_unacceptable_data(self):
        sllist = SinglyLinkedList()
        sllist.head = "a string"
        with pytest.raises(ValueError) as exc_info:
            sllist.target = ""
        assert "unacceptable" in str(exc_info)


class TestInsertAfterTarget:
    def test_insert_after_one_node(self):
        sllist = SinglyLinkedList(["foo"])
        sllist.insert_after_target("foo", "bar")
        assert getattr(sllist.head, "next") is getattr(sllist, "tail")
        assert getattr(sllist.tail, "data") == "bar"

    def test_insert_after_between_two_nodes(self):
        sllist = SinglyLinkedList(["foo", "bar"])
        sllist.insert_after_target("foo", "between nodes")
        assert getattr(sllist.head.next, "data") == "between nodes"

    def test_traverse_insert_after_before_tail(self):
        sllist = SinglyLinkedList(["foo", "bar", "moo", "shoe"])
        sllist.insert_after_target("moo", "before tail")
        assert getattr(sllist.head.next.next.next, "data") == "before tail"
        assert getattr(sllist.tail, "data") == "shoe"

    def test_traverse_insert_after_tail(self):
        sllist = SinglyLinkedList(["foo", "bar", "moo", "shoe"])
        sllist.insert_after_target("shoe", "after tail")
        assert getattr(sllist.head.next.next.next, "data") == "shoe"
        assert getattr(sllist.tail, "data") == "after tail"

    def test_first_encounter(self):
        sllist = SinglyLinkedList(["foo", "bar", "bar"])
        first_encounter = getattr(sllist.head, "next")
        sllist.insert_after_target("bar", "biz")
        assert getattr(sllist.head, "next") is first_encounter
        assert getattr(sllist.head.next.next, "data") == "biz"

    def test_no_target_match(self):
        sllist = SinglyLinkedList(["foo", "bar"])
        assert sllist.insert_after_target("baz", "new node") is False

    def test_no_target_match_empty_list(self):
        sllist = SinglyLinkedList()
        assert sllist.insert_after_target("baz", "new node") is False

class TestInsertBeforeTarget:
    def test_insert_before_head(self):
        sllist = SinglyLinkedList(["foo", "bar"])
        sllist.insert_before_target("foo", "before head")
        assert getattr(sllist.head, "data") == "before head"
        assert getattr(sllist.head.next, "data") == "foo"

    def test_traversal_before_tail(self):
        sllist = SinglyLinkedList(["foo", "bar", "baz"])
        sllist.insert_before_target("baz", "before tail")
        assert getattr(sllist.tail, "data") == "baz"
        assert getattr(sllist.head.next.next, "data") == "before tail"

    def test_no_target_match(self):
        sllist = SinglyLinkedList(["foo", "bar"])
        assert sllist.insert_before_target("baz", "new node") is False

    def test_no_target_match_empty_list(self):
        sllist = SinglyLinkedList()
        assert sllist.insert_before_target("baz", "new node") is False


class TestSortingInstanceMethods:

    def test_bubble_sort_descending(self):
        sllist = SinglyLinkedList([8, 2, 6, 4, 5])
        sllist.bubble_sort(ascending=False)
        assert repr(sllist) == "SinglyLinkedList([8, 6, 5, 4, 2])"
        assert str(sllist) == "8 -> 6 -> 5 -> 4 -> 2"

    def test_insertion_sort_ascending(self):
        sllist = SinglyLinkedList([8, 2, 6, 4, 5])
        sllist.insertion_sort()
        assert repr(sllist) == "SinglyLinkedList([2, 4, 5, 6, 8])"
        assert str(sllist) == "2 -> 4 -> 5 -> 6 -> 8"

    def test_insertion_sort_descending_custom_key(self):
        # Custom comparison function
        def by_length(s):
            return len(s)

        sllist = SinglyLinkedList(['date', 'peach', 'cherry', 'strawberry'])
        sllist.insertion_sort(ascending=False, key=by_length)
        assert repr(sllist) == "SinglyLinkedList(['strawberry', 'cherry', 'peach', 'date'])"

    def test_reverse_order(self):
        sllist = SinglyLinkedList()
        with pytest.raises(ValueError) as exc_info:
            sllist.reverse_order()
        assert "empty linked list" in str(exc_info)
        sllist = SinglyLinkedList([8, 2, 6, 4, 5])
        sllist.reverse_order()
        assert repr(sllist) == "SinglyLinkedList([5, 4, 6, 2, 8])"
        assert str(sllist) == "5 -> 4 -> 6 -> 2 -> 8"
