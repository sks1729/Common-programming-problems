"""
    Given a singly linked list write a function which takes in the first node
    of the list and return a boolean if the linked list contains a cycle

    This linked list in this case is also known as circularly linked list

    Logic behind the solution
    We assume two runners at the starting of a track
    marker1 and marker2 are two markers which start at the first node
    marker2 moves 2 nodes ahead for every node that marker1 moves.

    If the track were a straight track, marker2 would never meet marker1.
    Since marker2 moves faster than marker1, if marker2 crosses marker1 (lapping)
    the linked list is circular
"""

# create singly linked list node class
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


# node parameter = first node
def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next_node != None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True

    return False


# CYCLE
a = Node(1)
b = Node(1)
c = Node(1)

a.next_node = b
b.next_node = c
c.next_node = a

# NON-CYCLE
x = Node(1)
y = Node(2)
z = Node(2)

x.next_node = y
y.next_node = z

# first node argument = a
print(cycle_check(a))  # True

# first node argument = x
print(cycle_check(x))  # False
