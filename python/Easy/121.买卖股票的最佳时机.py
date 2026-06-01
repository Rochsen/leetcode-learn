"""
121. 买卖股票的最佳时机

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]
        max_earn = 0
        
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                if current_profit > max_earn:
                    max_earn = current_profit
        
        return max_earn



class Solution:
    """超时"""
    def maxProfit(self, prices: List[int]) -> int:
        max_earn = 0

        for idx in range(len(prices)-1):
            buy_point = prices[idx]

            for idj in range(idx+1, len(prices)):
                sol_point = prices[idj]
                if buy_point >= sol_point:
                    continue
                else:
                    tmp_max_earn = sol_point - buy_point
                    if tmp_max_earn > max_earn:
                        max_earn = tmp_max_earn
                    else:
                        pass

        return max_earn


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
