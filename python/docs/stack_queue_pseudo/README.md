# stack-queue-pseudo

## Whiteboard Process
[White Board Link](https://arrayreverse.invisionapp.com/freehand/Untitled-bKhpukJj)
![whiteboard](./whiteboard12.png)

## Approach & Efficiency
The PseudoQueue utilizes a two-stack approach for implementing enqueue and dequeue operations. Enqueueing a value is a constant-time operation, as it involves pushing onto the first stack. Dequeueing, while potentially requiring a transfer from the first stack to the second, remains an amortized constant-time operation. This design ensures an efficient simulation of a queue, with the occasional cost of transferring elements balanced by frequent constant-time operations. The space complexity is O(n), where n is the total number of elements in the PseudoQueue, considering both stacks. This approach provides an effective and balanced solution for scenarios requiring efficient first-in, first-out operations.

## Solution
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class PseudoQueue:
    def __init__(self):
        # Two stacks to implement the PseudoQueue
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        # Push the value onto stack1
        self.stack1.push(value)

    def dequeue(self):
        # Check if both stacks are empty
        if self.stack1.is_empty() and self.stack2.is_empty():
            return None

        # If stack2 is empty, transfer elements from stack1 to stack2
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        # Pop the front element from stack2
        return self.stack2.pop()


# usage:

# Example usage:
pseudo_queue = PseudoQueue()
pseudo_queue.enqueue(10)
pseudo_queue.enqueue(15)
pseudo_queue.enqueue(20)

print("Internal State after enqueue:")
print("Stack1:", pseudo_queue.stack1.items)
print("Stack2:", pseudo_queue.stack2.items)

dequeued_value = pseudo_queue.dequeue()
print("\nDequeued value:", dequeued_value)

print("\nInternal State after dequeue:")
print("Stack1:", pseudo_queue.stack1.items)
print("Stack2:", pseudo_queue.stack2.items)