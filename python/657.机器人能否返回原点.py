"""
657. 机器人能否返回原点

在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 (0, 0) 处结束。

移动顺序由字符串 moves 表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。

如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。

注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R')

        # zero_point = [0, 0]

        # for char in moves:
        #     if char == 'U':
        #         zero_point[-1] += 1
        #     elif char == 'D':
        #         zero_point[-1] -= 1
        #     elif char == 'L':
        #         zero_point[0] -= 1
        #     else:
        #         zero_point[0] += 1
        
        # return zero_point[0] == 0 and zero_point[-1] == 0
