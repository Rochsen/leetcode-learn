"""
66. Plus One

给定一个表示 大整数 的整数数组 digits，其中 digits[i] 是整数的第 i 位数字。这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导 0。

将大整数加 1，并返回结果的数字数组。

示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
加 1 后得到 123 + 1 = 124。
因此，结果应该是 [1,2,4]。

示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
加 1 后得到 4321 + 1 = 4322。
因此，结果应该是 [4,3,2,2]。

示例 3：

输入：digits = [9]
输出：[1,0]
解释：输入数组表示数字 9。
加 1 得到了 9 + 1 = 10。
因此，结果应该是 [1,0]。

"""
from typing import List


class Solution:
    """
    AI写的, 思路是，不管数字多大，都只会传递加1
    从后往前遍历，如果当前数字不是9，则加1，并返回结果。
    如果当前数字是9，则将当前数字改为0，并继续遍历。如果遍历结束，并且当前数字 still 9，则将当前数字改为0，并插入一个1到结果列表的开头。
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            print("i=", i)
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits



if __name__ == '__main__':
    s = Solution()
    # print(s.plusOne([1, 2, 3]))

    # print(s.plusOne([4, 3, 2, 1]))

    print(s.plusOne([9]))

    print(s.plusOne([5, 8, 9, 9]))

    print(s.plusOne([0]))