"""
    Singly linked list is a data structure having a collection of
    nodes that collectively form a linear sequence.

    first and last node of the list are called
    head and tail respectively

    nothing points to head of the list
    whereas the last node points to None
    last node is the node having None as its next reference

    going through the nodes of the list is called traversing
    the next reference of a node can be called as link or pointer,
    so traversing a linked list is also known as link or pointer hopping
"""


# Singly linked list Node
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


a = Node(1)
b = Node(2)
c = Node(3)
a.next_node = b
b.next_node = c

print(a.next_node.value)
