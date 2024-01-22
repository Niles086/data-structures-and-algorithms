from stack_and_queue import Stack, Queue

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
