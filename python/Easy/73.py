"""
@File    :   73.py
@Time    :   2026/02/27
@Title   :   73. 矩阵置零
@Difficulty:  Medium
@Desc    :   给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_has_zero = [0 in row for row in matrix]  # 行是否包含 0
        col_has_zero = [0 in col for col in zip(*matrix)]  # 列是否包含 0

        for i, row0 in enumerate(row_has_zero):
            for j, col0 in enumerate(col_has_zero):
                if row0 or col0:  # i 行或 j 列有 0
                    matrix[i][j] = 0  # 题目要求原地修改，无返回值

        # find_zero_p_row = []
        # find_zero_p_col = []

        # for idx, lnum1 in enumerate(matrix):
        #     for idj, lnum2 in enumerate(lnum1):
        #         if lnum2 == 0:
        #             find_zero_p_row.append(idx)
        #             find_zero_p_col.append(idj)

        # print(find_zero_p_row)
        # print(find_zero_p_col)

        # for idx in find_zero_p_row:
        #     matrix[idx] = [0] * len(matrix[idx])
        # for idj in find_zero_p_col:
        #     for i in range(len(matrix)):
        #         matrix[i][idj] = 0

    


if __name__ == "__main__":
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    Solution().setZeroes(matrix)