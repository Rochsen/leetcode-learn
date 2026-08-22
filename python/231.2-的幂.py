#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#
import math


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return math.log2(n) == int(math.log2(n))


# @lc code=end
