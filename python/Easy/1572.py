"""
@File    :   1572.py
@Time    :   2026/02/27
@Title   :   1572. 矩阵对角线元素的和
@Difficulty:  Easy
@Desc    :   给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
"""
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        mat_size = len(mat)

        major_p = list(zip(range(mat_size), range(mat_size)))
        other_p = list(zip(range(mat_size), range(mat_size)[::-1]))

        res = 0

        all_p = set(major_p + other_p)

        for i,j in all_p:
            res += mat[i][j]

        return res


if __name__ == "__main__":
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    print(Solution().diagonalSum(mat))