# 491. Palindrome Number
# Check a positive number is a palindrome or not.

# A palindrome number is that if you reverse the whole number you will get exactly the same number.

# Example
# 11, 121, 1, 12321 are palindrome numbers.

# 23, 32, 1232 are not palindrome numbers.

class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        # write your code here
        
        if num < 0:
            return False
        tmp = num
        rev = 0 
        while tmp > 0:
            rev = rev * 10 + tmp % 10
            tmp //= 10
        return rev == num
        


            
