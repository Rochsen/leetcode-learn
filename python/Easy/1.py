"""
1. 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
 
进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
"""
from typing import List


class SolutionVio:
    """暴力解法 4289ms 击败5.00%"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for start_idx, start_num in enumerate(nums):
            for next_idx, next_num in enumerate(nums):
                if start_idx != next_idx and start_num + next_num == target:
                    return [start_idx, next_idx]

        return []
    

class SolutionLinear:
    """线性查找 351ms 击败31.64%"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, first_num in enumerate(nums):
            next_num = target - first_num
            next_nums = nums[idx+1:]
            if next_num in next_nums:
                return [idx, next_nums.index(next_num)+idx+1]
            else:
                continue

        return []
    

class Solution:
    """哈希表 3ms 击败56.93%"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # 值到下标的映射
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:  # 找到匹配
                return [seen[complement], idx]
            
            seen[num] = idx  # 存入当前值及其下标
            
        return []  # 题目保证有解，这里仅为语法完整


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))

    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))

    nums = [3, 3]
    target = 6
    print(Solution().twoSum(nums, target))