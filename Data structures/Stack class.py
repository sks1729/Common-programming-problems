"""
    Stack data structure is similar to pile of books on a table
    the end is commonly referred as "top"
    the end opposite to the top is commonly referred as "base"

    Stack allows user to add item only at the END or TOP,
    and remove item only from the END or BASE

    ordering principle:
    Last In First Out (LIFO)
"""


class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # similar to adding a new book at the top of the pile of books
    def push(self, item):
        self.items.append(item)

    # similar to taking out the book at the top of the pile
    def pop(self):
        self.items.pop()

    # similar to viewing the book at the top of the pile
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


s = Stack()

print(s.is_empty())
