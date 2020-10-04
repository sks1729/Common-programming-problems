"""
    Queue data structure is similar to a movie ticket line
    The first person in the line is the first one served

    Queue ordering principle:
    First In First Out (FIFO)
    first-come first-serve

    Queue allows user to add item only at the END or REAR,
    and remove item only from the FRONT
"""


class Queue(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


q = Queue()

q.enqueue(1)
q.enqueue(12)
q.enqueue(13)

print(q)

q.dequeue()

print(q)
