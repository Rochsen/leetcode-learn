#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_p = s.split(" ")

        return len(pattern) == len(s_p) and len(set(zip(pattern, s_p))) == len(
            set(s_p)
        ) == len(set(pattern))


# @lc code=end
