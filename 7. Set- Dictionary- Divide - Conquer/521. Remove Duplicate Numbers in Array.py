# 521. Remove Duplicate Numbers in Array
# Given an array of integers, remove the duplicate numbers in it.

# You should:

# Do it in place in the array.
# Move the unique numbers to the front of the array.
# Return the total number of the unique numbers.
# Example
# Given nums = [1,3,1,4,4,2], you should:

# Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
# Return the number of unique integers in nums => 4.

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        d, result = {}, 0
        for num in nums:
            if num not in d:
                d[num] = True
                nums[result] = num
                result += 1
            print(d.keys())

        return result
