#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from typing import list


# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """参考了贪心算法的思路"""
        max_index = len(nums) - 1       # 数组索引最大值
        start_index = 0                 # 起始位置
        result = nums[0]                # 返回结果
        count = 0                       # 临时计算存储结果

        # 单向遍历数组
        while start_index <= max_index:
            count += nums[start_index]   # 临时存储的结果 + 当前索引的值
            result = max(count, result)  # result取当前最大的计算值
            start_index += 1             # 索引位置更新
            count = max(count, 0)        # count 比0小，重置

        return result


# @lc code=end
