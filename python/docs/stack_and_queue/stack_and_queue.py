class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop from an empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None

class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
        else:
            current = self.front
            while current.next:
                current = current.next
            current.next = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Cannot dequeue from an empty queue")
        value = self.front.value
        self.front = self.front.next
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty queue")
        return self.front.value

    def is_empty(self):
        return self.front is None
