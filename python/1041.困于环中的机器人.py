"""
@File    :   1041.py
@Time    :   2026/02/27
@Title   :   1041. 困于环中的机器人
@Difficulty:  Medium
@Desc    :   在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。注意:

北方向 是y轴的正方向。
南方向 是y轴的负方向。
东方向 是x轴的正方向。
西方向 是x轴的负方向。
机器人可以接受下列三条指令之一：

"G"：直走 1 个单位
"L"：左转 90 度
"R"：右转 90 度
机器人按顺序执行指令 instructions，并一直重复它们。

只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        k = 0
        dist = [0] * 4
        for c in instructions:
            if c == 'L':
                k = (k + 1) % 4
            elif c == 'R':
                k = (k + 3) % 4
            else:
                dist[k] += 1
        return (dist[0] == dist[2] and dist[1] == dist[3]) or k != 0

