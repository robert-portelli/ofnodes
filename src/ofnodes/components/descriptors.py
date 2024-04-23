from ofnodes.nodes.singlynode import SinglyNode

class Head:
    def __get__(self, instance, owner):
        """Getter method for the head of the linked list."""
        return instance._head

    def __set__(self, instance, value):
        if isinstance(value, SinglyNode):
            node = value
            #return
        else:
            node = SinglyNode(value)

        if instance._head is None:
            instance._head = node
            instance._tail = node
        else:
            setattr(node, '_next', instance._head)
            instance._head = node

    def __delete__(self, instance):
        """Deleter method for the head of the linked list."""
        raise AttributeError(
            f"{type(instance).__name__}'s `head` attribute " "cannot be deleted."
        )