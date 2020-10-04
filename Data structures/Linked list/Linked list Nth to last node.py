"""
    function that takes a head node and an integer value n and return
    the nth node to the last node in the linked list

    Logic behind the solution
    Consider a collection of nodes, and length of the collection is L
    take two pointers (markers) left_pointer and right_pointer at the head node

    If we take the right_pointer to the Nth node from the head node,
    L - N nodes are left from the tail node to the right_pointer
    keeping the left_pointer at the head node itself

    Now, if we increase the position of the left_pointer and right_pointer by one node
    at the same time until the right_pointer reaches the tail node,
    the left_pointer lands at the (L - N)th node to the first node,
    which is Nth node to last node
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n - 1):
        if not right_pointer.next_node:
            raise LookupError("Error: n is larger than the linked list")

        right_pointer = right_pointer.next_node

    while right_pointer.next_node:
        left_pointer = left_pointer.next_node
        right_pointer = right_pointer.next_node

    return left_pointer


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

target_node = nth_to_last_node(4, a)
print(target_node.value)
