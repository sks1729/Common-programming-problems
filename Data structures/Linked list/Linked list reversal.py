"""
    Write a function to reverse a linked list. The function will take in
    head node and return new head node of the reversed list.

    Logic behind the solution
    we can reverse the list by changing the next pointer of each node to
    the previous node
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


# head parameter = first or head node
def reverse(head):
    current = head
    previous = None

    while current:
        next_node = current.next_node
        current.next_node = previous

        previous = current
        current = next_node
    return previous


A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)

A.next_node = B
B.next_node = C
C.next_node = D

# reversing the linked list with node A as the head node
# first head argument = A
reverse(A)

# since the Linked list is reversed, new order of the nodes:
# D -> C -> B -> A

# node A references to None
print(A.next_node)  # None

# node D references to node C and node C has value 3
print(D.next_node.value)  # 3
