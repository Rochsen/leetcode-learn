#
# @lc app=leetcode.cn id=3622 lang=python3
#
# [3622] 判断整除性
#

# @lc code=start
from math import prod


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n < 10:
            return False
        
        # 1. 获取数字列表
        list_digits = [int(i) for i in str(n)]

        # 2. 获取数字列表的 summary
        summary = sum(list_digits) + prod(list_digits)

        return n % summary == 0
        
# @lc code=end

