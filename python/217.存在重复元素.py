#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#
from typing import List
from collections import Counter

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        return len([c for c in cnt.values() if c > 1]) > 0
    
# @lc code=end

