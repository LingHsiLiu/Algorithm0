# 492. Implement Queue by Linked List
# Implement a Queue by linked list. Support the following basic methods:

# enqueue(item). Put a new item in the queue.
# dequeue(). Move the first item out of the queue, return it.
# Example
# enqueue(1)
# enqueue(2)
# enqueue(3)
# dequeue() // return 1
# enqueue(4)
# dequeue() // return 2


class MyQueue:
    def __init__(self):
        # do some intialize if necessary
        self.first, self.last = None, None

    # @param {int} item an integer
    # @return nothing
    def enqueue(self, item):
        # Write yout code here
        if self.first is None:
            self.first = Node(item)
            self.last = self.first
        else:
            self.last.next = Node(item)
            self.last = self.last.next

    # @return an integer
    def dequeue(self):
        # Write your code here
        if self.first is not None:
            item = self.first.val
            self.first = self.first.next
            return item

        return -1000

class Node():

    def __init__(self, _val):
        self.next = None
        self.val = _val
