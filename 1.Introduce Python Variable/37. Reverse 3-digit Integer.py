# 37. Reverse 3-digit Integer
# Reverse a 3-digit integer.

# Example
# Reverse 123 you will get 321.

# Reverse 900 you will get 9.

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        num1 = number % 10
        num2 = (number // 10 ) % 10
        num3 = number // 100
        return num1 * 100 + num2 * 10 + num3
