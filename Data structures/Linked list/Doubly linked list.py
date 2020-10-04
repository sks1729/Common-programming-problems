"""
    Doubly linked list is a data structure having a collection of nodes,
    in which each node has reference to the node before it and after it
    The main difference between single and doubly linked list is that
    doubly linked list has reference to nodes both to previous and next nodes

    special nodes (header node and trailer node) are added at ends of the list
    header node at the beginning and trailer at the end
    These special nodes (dummy nodes) are known as sentinels or guards
"""


# Doubly linked list Node
class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev_node = None
        self.next_node = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b

