#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List
from functools import reduce


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dict_phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # 初始化为包含一个空字符串的列表
        result = [""]

        for digit in digits:
            # 对于每一个新的数字，将现有结果中的每个字符串与新数字对应的每个字母拼接
            next_result = []
            print(f"digit = {digit}")

            for prefix in result:
                print(f"prefix = {prefix}")
                for letter in dict_phone[digit]:
                    print(f"letter = {letter}")
                    next_result.append(prefix + letter)

                print(f"next_result = {next_result}")

            result = next_result

            print(f"result = {result}")

        return result


if __name__ == '__main__':
    sol = Solution()

    print(sol.letterCombinations("23"))


# @lc code=end
