# 172. Remove Element
# Given an array and a value, remove all occurrences of that value in place and return the new length.

# The order of elements can be changed, and the elements after the new length don't matter.

# Example
# Given an array [0,4,4,0,0,2,4,4], value=4

# return 4 and front four elements of the array is [0,0,0,2]

class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        j = len(A)-1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        print(j+-1)
        return j+1
