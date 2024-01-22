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

# Tests
def test_stack():
    stack = Stack()
    assert stack.is_empty() is True

    stack.push(1)
    stack.push(2)
    assert stack.is_empty() is False
    assert stack.pop() == 2
    assert stack.peek() == 1
    assert stack.pop() == 1
    assert stack.is_empty() is True

    try:
        stack.pop()
    except Exception as e:
        assert str(e) == "Cannot pop from an empty stack"

    try:
        stack.peek()
    except Exception as e:
        assert str(e) == "Cannot peek an empty stack"

def test_queue():
    queue = Queue()
    assert queue.is_empty() is True

    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.is_empty() is False
    assert queue.dequeue() == 1
    assert queue.peek() == 2
    assert queue.dequeue() == 2
    assert queue.is_empty() is True

    try:
        queue.dequeue()
    except Exception as e:
        assert str(e) == "Cannot dequeue from an empty queue"

    try:
        queue.peek()
    except Exception as e:
        assert str(e) == "Cannot peek an empty queue"

if __name__ == "__main__":
    test_stack()
    test_queue()
