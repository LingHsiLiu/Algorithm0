# 464. Sort Integers II
# Given an integer array, sort it in ascending order. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

# Example
# Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        i = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]
