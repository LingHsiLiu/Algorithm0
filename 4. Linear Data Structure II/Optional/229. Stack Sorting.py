# 229. Stack Sorting
# Sort a stack in ascending order (with biggest terms on top).

# You may use at most one additional stack to hold items, but you may not copy the elements into any other data structure (e.g. array).

# You don't need to return a new stack, just sort elements in the given parameter stack.

# Example
# Given stack =

# | |
# |3|
# |1|
# |2|
# |4|
#  -
# After sort, the stack should become:

# | |
# |4|
# |3|
# |2|
# |1|
#  -
# The data will be serialized to [4,2,1,3]. The last element is the element on the top of the stack.


"""
In python, you can use list as stack
stack = [1,2,3,4]
Get top element: stack[-1]  -> 4
Pop element: stack.pop()   -> 4
Push element: stack.append(5)
check the size of stack: len(stack)
"""


class Solution:
    """
    @param: stk: an integer stack
    @return: void
    """
    def stackSorting(self, stk):
        # write your code here
