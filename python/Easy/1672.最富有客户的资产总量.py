"""
@File    :   1672.py
@Time    :   2026/02/27
@Title   :   1672. 最富有客户的资产总量
@Difficulty:  Easy
@Desc    :   给你一个 m x n 的整数网格 accounts ，其中 accounts[i][j] 是第 i​​​​​​​​​​​​ 位客户在第 j 家银行托管的资产数量。返回最富有客户所拥有的 资产总量 。
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)