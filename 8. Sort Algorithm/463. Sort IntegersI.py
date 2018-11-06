# 463. Sort Integers
# Given an integer array, sort it in ascending order. Use selection sort, bubble sort, insertion sort or any O(n2) algorithm.

# Example
# Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].

# 插入法

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        for i in range(len(A)):
            newval= A[i]
            j = i-1
            
            while (j >=0 and A[j] > newval):
                A[j+1] = A[j]
                j -= 1
            
            A[j+1] = newval
