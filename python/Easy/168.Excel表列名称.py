"""
168. Excel 表列名称
简单
相关标签
premium lock icon
相关企业
给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
"""


class Solution:
    """
    chr函数将整数转换为对应的字符
    """
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            print(f"1res={res}")
            res = chr(columnNumber % 26 + ord('A')) + res
            print(f"2res={res}")
            columnNumber //= 26
            
        return res

"""
执行 convertToTitle(columnNumber = 1) 输出为："A"
执行 convertToTitle(columnNumber = 28) 输出为："AB"
执行 convertToTitle(columnNumber = 701) 输出为："ZY"
执行 convertToTitle(columnNumber = 2147483647) 输出为："FXSHRXW"
提示：
1 <= columnNumber <= 231 - 1
"""
# 测试代码
if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(1))
    print(s.convertToTitle(28))
    print(s.convertToTitle(701))
    print(s.convertToTitle(2147483647))