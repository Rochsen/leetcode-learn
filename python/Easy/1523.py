"""
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

countOdds(low = 3, high = 7) == 3
countOdds(low = 8, high = 10) == 1

Constraints:
0 <= low <= high <= 10^9
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return len([i for i in range(low, high+1) if i % 2 != 0])