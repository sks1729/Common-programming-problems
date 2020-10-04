"""
    Deque = double-ended queue
    Deque is a hybrid data structure of Stack and Queue structures

    the two ends of the Deque are Front and Rear (back)
    items can be added or removed from both ends of the structure
    or, it can be expanded or contracted from both ends
"""


# [1, 6, 1, 8, 0]
# I have taken the index 0 as front and index -1 as REAR (back)
class Deque(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop(0)

    def add_rear(self, item):
        self.items.append(item)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
