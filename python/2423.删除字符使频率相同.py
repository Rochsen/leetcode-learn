#
# @lc app=leetcode.cn id=2423 lang=python3
#
# [2423] 删除字符使频率相同
#

# @lc code=start
from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:

        for i in range(len(word)):
            word_copy = word[: i] + word[i+1:]

            res = set(Counter(word_copy).values())

            if len(res) == 1:
                return True
            
        return False

            


        
# @lc code=end

