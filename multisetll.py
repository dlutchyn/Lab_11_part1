from node import *

# A class implementing Multiset as a linked list.


class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.

        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.

        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head is None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.

        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current is not None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """
        Removes a value from multiset.

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def remove_all(self):
        """
        Removes all items from multiset and returns values in its nodes
        by generator.
        """
        while self._head is not None:
            yield self._head
            self._head = self._head.next

    def split_half(self):
        """
        Splits the multiset in two halves and returns pointers (links)
        on these two halves. Returns None if the multiset has 1 element.

        :return: tuple(Node, Node)
        """
        if self._head.next.next is None:
            return None

        pointer1 = self._head
        pointer2 = self._head
        while pointer2 is not None and pointer2.next is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
        multiset2 = pointer1.next
        pointer1.next = None
        multiset1 = self._head
        return (multiset1,  multiset2)

    @staticmethod
    def extend(head, head1):
        """
        Returns a pointer (link) on the extended multiset from
        two given multisets.

        :param head: Node (first element (head) of first multiset)
        :param head1: Node (first element (head) of second multiset)
        :return: Node (pointer on a start of extended multiset)
        """

        pointer_start = head
        pointer = head
        pointer1 = head1

        while pointer.next is not None:
            pointer = pointer.next

        while pointer1 is not None:
            pointer.next = pointer1
            pointer = pointer.next
            pointer1 = pointer1.next

        return pointer_start

    @staticmethod
    def represent_multiset(head):
        """
        Prints all nodes (values) of a multiset.
        """
        while head is not None:
            print(head)
            head = head.next


if __name__ == "__main__":

    # create a multiset
    mulset = Multiset()

    # add nodes to the multiset.
    mulset.add(1)
    mulset.add(2)
    mulset.add(3)
    mulset.add(4)
    mulset.add(4)
    mulset.add(5)

    # print out all nodes (items) from multiset.
    mulset.represent_multiset(mulset._head)
    print('--------------------')

    # remove node
    mulset.delete(4)

    mulset.represent_multiset(mulset._head)
    print('--------------------')

    # split our multiset in half
    node1, node2 = mulset.split_half()

    print('First half (multiset1):')
    Multiset.represent_multiset(node1)
    print('Second half (multiset2):')
    Multiset.represent_multiset(node2)

    print('-----------------------')

    # extend multiset1 with multiset2
    extended_multiset_start = mulset.extend(node1, node2)
    print('Extended multiset:')
    Multiset.represent_multiset(extended_multiset_start)

    print('-----------------------')

    # remove all elements from the multiset and print list of values
    print([el for el in mulset.remove_all()])
