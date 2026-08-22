"""
14. 最长公共前缀

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入:strs = ["flower","flow","flight"]
输出:"fl"

示例 2:
输入:strs = ["dog","racecar","car"]
输出:""
解释:输入不存在公共前缀。
"""


class Solution:
    """个人解法: 0ms 击败100.00%"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 找到最短的字符串长度
        min_len = min([len(s) for s in strs])
        # 存储结果
        same_string = ""
        # 遍历字符串长度
        for i in range(min_len):
            # 取第一个字符串的第一个字符
            tmp_char = strs[0][i]
            # 判断所有字符串的当前位置字符是否相同， 相同就添加到公共前缀字符串中
            if all([s[i] == tmp_char for s in strs]):
                same_string += tmp_char
            else:
                break
            
        return same_string
