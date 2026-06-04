#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import List

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dict_cnt = {}
        
        for n in nums:
            if n in dict_cnt:
                dict_cnt[n] += 1
            else:
                dict_cnt[n] = 1

        return [k for k,v in dict_cnt.items() if v == max(dict_cnt.values())][0]
        
# @lc code=end

