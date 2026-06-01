"""
1768. Merge Strings Alternately

给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。

返回 合并后的字符串 。
"""


class Solution:
    """不要zip"""
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            res += word1[i]
            res += word2[i]

        res += word1[min_len:]
        res += word2[min_len:]

        return res



class Solution:
    """有些多余"""
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        zip_list = list(zip(word1, word2))
        res = ""
        for item in zip_list:
            res += item[0]
            res += item[1]

        res += word1[min_len:]
        res += word2[min_len:]
        
        return res