# implement a Queue using two stacks

class QueueUsingStacks(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def __str__(self):
        return self.in_stack.extend(self.out_stack)

    def is_empty(self):
        return self.in_stack + self.out_stack == []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        # both stacks empty
        if len(self.in_stack) == 0 and len(self.out_stack) == 0:
            print("Queue is empty")
            return

        # out_stack is empty and in_stack has elements
        if not self.out_stack and self.in_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack.pop()

        return self.out_stack.pop()

    def size(self):
        return len(self.in_stack + self.out_stack)


q = QueueUsingStacks()

q.enqueue(1)

q.enqueue(2)

q.enqueue(3)

q.dequeue()

print(q.is_empty())

print(q)
