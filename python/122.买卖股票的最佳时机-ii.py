#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        list_erch = [prices[idx + 1] - prices[idx] for idx in range(len(prices) - 1)]
        return sum([e for e in list_erch if e > 0])


# @lc code=end


if __name__ == "__main__":
    sol = Solution()

    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
