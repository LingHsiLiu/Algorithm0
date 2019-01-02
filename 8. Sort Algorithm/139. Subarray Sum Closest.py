# 139. Subarray Sum Closest
# Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.

# Example
# Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4].

# Challenge
# O(nlogn) time

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
