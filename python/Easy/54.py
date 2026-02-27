"""
@File    :   54.py
@Time    :   2026/02/27
@Title   :   54. 螺旋矩阵
@Difficulty:  Medium
@Desc    :   给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res
