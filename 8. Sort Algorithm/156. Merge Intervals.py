# 156. Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.

# Example
# Given intervals => merged intervals:

# [                     [
#   (1, 3),               (1, 6),
#   (2, 6),      =>       (8, 10),
#   (8, 10),              (15, 18)
#   (15, 18)            ]
# ]
# Challenge
# O(n log n) time and O(1) extra space.


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
