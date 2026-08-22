"""
Excel 表列序号
给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。

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
    26进制转10进制
    """
    def titleToNumber(self, columnTitle: str) -> int:
        sum_num = 0

        for idx, char in enumerate(columnTitle):
            sum_num *= 26
            sum_num += ord(char) - ord('A') + 1
        
        return sum_num


if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("A"))