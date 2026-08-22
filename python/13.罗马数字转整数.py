"""
13. 罗马数字转整数

罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边 。

同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。



示例 1:
输入: s = "III"
输出: 3

示例 2:
输入: s = "IV"
输出: 4

示例 3:
输入: s = "IX"
输出: 9

示例 4:
输入: s = "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例 5:
输入: s = "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""


# 单罗马数字
SINGLE_ROMAN_DICT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# 多罗马数字组合
MULTI_ROMAN_DICT = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}


class SolutionSelf:
    """个人解法： 4ms 击败67.75%"""

    def romanToInt(self, s: str) -> int:
        # 用于存放计算结果
        result_sum = 0

        # 备份源字符串
        tmp_s = s

        while len(tmp_s) > 0:

            tmp_number = tmp_s[0]

            # 查找组合
            if tmp_number in ('I', 'X', 'C'):
                combo_number = tmp_s[0: 2]

                if combo_number in MULTI_ROMAN_DICT:
                    result_sum += MULTI_ROMAN_DICT[combo_number]
                    tmp_s = tmp_s[2:] if len(tmp_s) > 1 else ""
                else:
                    result_sum += SINGLE_ROMAN_DICT[tmp_number]
                    tmp_s = tmp_s[1:] if len(tmp_s) > 0 else ""

            else:
                result_sum += SINGLE_ROMAN_DICT[tmp_number]
                tmp_s = tmp_s[1:] if len(tmp_s) > 0 else ""

        return result_sum


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))


if __name__ == '__main__':
    s = "MCMXCIV"
    print(SolutionSelf().romanToInt(s))

    s = "MCMXCIV"
    print(Solution().romanToInt(s))
