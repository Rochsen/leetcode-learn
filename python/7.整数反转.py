#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        
        flag = 1
        
        if x < 0:
            x = -x
            flag = -1
        else:
            x = x
        
        s = int(str(x)[::-1])

        return flag * s if s < 2**31 else 0

        
# @lc code=end

