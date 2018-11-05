# 463. Sort Integers
# Given an integer array, sort it in ascending order. Use selection sort, bubble sort, insertion sort or any O(n2) algorithm.

# Example
# Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        self.quickSort(A, 0, len(A)-1)
        
    def quickSort(self, A, start, end):
        if start >= end:
            return
        
        splitpoint = self.partition(A, start, end)
        self.quickSort(A, start, splitpoint-1)
        self.quickSort(A, splitpoint+1, end)
        
    def partition(self, A, start, end):
        
        pivot = A[start]
        left, right = start+1, end
        
        while left <= right:
            while left <= right and A[left] <= pivot:
                left +=1
            while left <= right and A[right] >= pivot:
                right -=1
                
            if left <= right:
                A[left],A[right] = A[right], A[left]
                
        A[start], A[right] = A[right], A[start]
        
        return right
