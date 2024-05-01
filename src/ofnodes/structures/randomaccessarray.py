from ofnodes.sorting.mixins import BubbleSortMixin, ReverseOrderMixin
class RandomAccessArray(BubbleSortMixin, ReverseOrderMixin):
    """An array supporting random access with bubble sort and order reversal capabilities.

    This class represents an array that supports random access operations and also provides
    functionality for sorting elements using bubble sort algorithm and reversing the order
    of elements.

    Args:
        size (int): The size of the array.

    Attributes:
        _data (list): The underlying list to store array elements.

    Note:
        This class inherits from BubbleSortMixin and ReverseOrderMixin to leverage the
        bubble sort and order reversal functionalities.
    """
    def __init__(self, size):
        self._data = [None] * size

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def __dir__(self) -> list[str]:
        # Get the list of attributes and methods from the parent classes
        parent_dir = set(super().__dir__())
        # Filter out private attributes and methods
        excluded = {'_head', '_tail', '_target', 'reference_based_reverse_order', 'reference_based_bubble_sort','index_based_bubble_sort', 'index_based_reverse_order'}
        parent_dir = {attr for attr in parent_dir if attr not in excluded}
        # Return a sorted list of all attributes and methods
        return sorted(parent_dir)

    def __repr__(self):
        """Returns a string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        return f"RandomAccessArray({self._data})"

    def __str__(self):
        """Returns a string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        return f"[{', '.join(str(item) for item in self._data)}]"

    def bubble_sort(self, ascending=True):
        return super().index_based_bubble_sort(ascending)

    def reverse_order(self):
        return super().index_based_reverse_order()