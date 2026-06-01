"""
20. 有效的括号

给定一个只包括 '(', ')', '{', '}', '[', ']' 的字符串 s ,判断字符串是否有效。

有效字符串需满足:

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

示例 1:
输入:s = "()"
输出:true

示例 2:
输入:s = "()[]{}"
输出:true

示例 3:
输入:s = "(]"
输出:false

示例 4:
输入:s = "([])"
输出:true

示例 5:
输入:s = "([)]"
输出:false
"""

class SolutionSelf:
    """
    个人解法：参考了讨论，使用了replace方法，每次替换一对括号，直到字符串为空，或者无法替换为止。
    167ms 击败4.10%
    """
    def isValid(self, s: str) -> bool:
        for _ in range(len(s)):
            s = s.replace("()", "").replace("[]", "").replace("{}", "")

            if not s:
                return True
            
        return False


class Solution:
    """ 
    高人解法:
    https://leetcode.cn/problems/valid-parentheses/solutions/89144/zhu-bu-fen-xi-tu-jie-zhan-zhan-shi-zui-biao-zhun-d
    """
    def isValid(self, s: str) -> bool:
        dic = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]: 
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(i)
            
        return not stack


