"""
67. 二进制求和

给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
 
示例 1：
输入:a = "11", b = "1"
输出："100"

示例 2：
输入：a = "1010", b = "1011"
输出："10101"
"""


class Solution:
    """
    python可以通过int转化进制
    从整型回到二进制字符串，前缀带有0b，需要去除
    """
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return bin(a + b)[2:]


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("11", "1"))