# 54. String to Integer (atoi)
# Implement function atoi to convert a string to an integer.

# If no valid conversion could be performed, a zero value is returned.

# If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

# Example
# "10" => 10
# "-1" => -1
# "123123123123123" => 2147483647
# "1.0" => 1

class Solution:
    """
    @param str: A string
    @return: An integer
    """
    def atoi(self, str):
        # write your code here
