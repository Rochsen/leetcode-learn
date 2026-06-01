"""
1822. 数组元素积的符号
已知函数 signFunc(x) 将会根据 x 的正负返回特定值：

如果 x 是正数，返回 1 。
如果 x 是负数，返回 -1 。
如果 x 是等于 0 ，返回 0 。
给你一个整数数组 nums 。令 product 为数组 nums 中所有元素值的乘积。

返回 signFunc(product) 。
"""


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        :param nums: List[int]
        :return: int
        """
        res = 1
        for n in nums:
            if n == 0: return 0
            if n < 0: res *= -1
        
        return res
        
        # from functools import reduce

        # val = reduce(lambda x,y: x*y, nums)

        # if val > 0:
        #     return 1
        # elif val < 0:
        #     return -1
        # else:
        #     return 0