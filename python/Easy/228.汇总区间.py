#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import List

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        if len(nums) == 1:
            return [f"{nums[0]}"]

        # 左区间位置，右区间位置
        left, right = 0, 0
        # 全部结果，单个连续区间的结果
        list_result, tmp_area = [], [f"{nums[left]}", f"{nums[right]}"]

        while right != len(nums) - 1:
            right += 1

            # 计算区间差值
            diff = nums[right] - nums[left]

            if diff == 1:
                tmp_area[-1] = f"{nums[right]}"
                print(f"tmp_area = {tmp_area}")

                # 遇到最后一个范围时不再进入循环了
                if right == len(nums) - 1:
                    list_result.append("->".join(tmp_area))
            else:
                if tmp_area[0] == tmp_area[-1]:
                    tmp_area.pop()

                list_result.append("->".join(tmp_area))
                tmp_area = [f"{nums[right]}", f"{nums[right]}"]

                # 遇到最后一个范围时不再进入循环了
                if right == len(nums) - 1:
                    list_result.append(f"{nums[right]}")

            left += 1

        return list_result

# @lc code=end


if __name__ == '__main__':
    sol = Solution()

    t1 = sol.summaryRanges([0, 1, 2, 4, 5, 7])
    print(f"t1 = {t1}")

    t2 = sol.summaryRanges([0, 2, 3, 4, 6, 8, 9])
    print(f"t2 = {t2}")

    t3 = sol.summaryRanges([0, 1, 2])
    print(f"t3 = {t3}")
