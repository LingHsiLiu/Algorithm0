# 31. Partition Array
# Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

# All elements < k are moved to the left
# All elements >= k are moved to the right
# Return the partitioning index, i.e the first index i nums[i] >= k.

# Example
# If nums = [3,2,2,1] and k=2, a valid answer is 1.

# Challenge
# Can you partition the array in-place and in O(n)?

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
