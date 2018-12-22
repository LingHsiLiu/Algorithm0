# 478. Simple Calculator
# Given two integers a and b, an operator, choices:

# +, -, *, /
# Calculate a <operator> b.

# Example
# For a = 1, b = 2, operator = +, return 3.

# For a = 10, b = 20, operator = *, return 200.

# For a = 3, b = 2, operator = /, return 1. (not 1.5)

# For a = 10, b = 11, operator = -, return -1.

class Calculator:
    """
    @param a: An integer
    @param operator: A character, +, -, *, /.
    @param b: An integer
    @return: The result
    """
    def calculate(self, a, operator, b):
        # write your code here
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b
