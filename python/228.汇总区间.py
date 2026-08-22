#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import List


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        res = []

        i = 0
        while i < n:
            left = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            right = nums[i]
            if left == right:
                res.append(str(left))
            else:
                res.append(f"{left}->{right}")
            i += 1
        return res


# @lc code=end


if __name__ == '__main__':
    sol = Solution()

    t1 = sol.summaryRanges([0, 1, 2, 4, 5, 7])
    print(f"t1 = {t1}")

    t2 = sol.summaryRanges([0, 2, 3, 4, 6, 8, 9])
    print(f"t2 = {t2}")

    t3 = sol.summaryRanges([0, 1, 2])
    print(f"t3 = {t3}")
