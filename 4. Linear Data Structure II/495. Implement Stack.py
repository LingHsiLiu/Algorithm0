# 495. Implement Stack
# Implement a stack. You can use any data structure inside a stack except stack itself to implement it.

# Example
# push(1)
# pop()
# push(2)
# top()  // return 2
# pop()
# isEmpty() // return true
# push(3)
# isEmpty() // return false


class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.queue = []
    
    def push(self, x):
        # write your code here
        self.queue.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        for x in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        self.queue.pop(0)

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        top = None
        for x in range(len(self.queue)):
            top = self.queue.pop(0)
            self.queue.append(top)
        return top

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return self.queue == []
