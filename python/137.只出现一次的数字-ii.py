#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
from functools import reduce
from typing import List

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        dict_count = {}

        for n in nums:
            if n in dict_count:
                dict_count[n] += 1
            else:
                dict_count[n] = 1

        return [k for k, v in dict_count.items() if v == 1][0]

# @lc code=end
