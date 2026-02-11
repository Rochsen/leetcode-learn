"""
9. 回文数

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。
"""


class SolutionTransString:
    """转化为字符实现：4ms 击败80.62%"""

    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


class Solution:
    """非字符实现：6ms 击败71.18%"""
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        rev = 0
        while rev < x // 10:
            rev = rev * 10 + x % 10
            x //= 10

        return rev == x or rev == x // 10


if __name__ == '__main__':
    print(Solution().isPalindrome(121))
