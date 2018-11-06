# 56. Two Sum
# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

# Example
# numbers=[2, 7, 11, 15], target=9

# return [0, 1]

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        for i, a in enumerate(numbers):
            for j, b in enumerate(numbers[i+1:]):
            # for j, b in enumerate(numbers[i+1-len(numbers):]):
                if a + b == target:
                    return [i, j+i+1]
        return [-1, -1]
        
