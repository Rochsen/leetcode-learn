#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:

    BIG = 2**30

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and Solution.BIG % n == 0

        
# @lc code=end

