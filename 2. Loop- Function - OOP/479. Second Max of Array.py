# 479. Second Max of Array
# Find the second max number in a given array.

# Example
# Given [1, 3, 2, 4], return 3.

# Given [1, 2], return 1.

class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        # write your code here
        maxValue = max(nums[0], nums[1])
        secValue = min(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            if (nums[i] > maxValue):
                secValue = maxValue
                maxValue = nums[i]
            elif (nums[i] > secValue):
                secValue = nums[i]
            
        return secValue
