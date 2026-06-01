"""
@File    :   1275.py
@Time    :   2026/02/27
@Title   :   1275. 找出井字游戏获胜者
@Difficulty:  Easy
"""

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        lista = []
        listb = []
        for step in range(0,(len(moves)),2):
            lista.append(moves[step])
        for step in range(1,(len(moves)),2):
            listb.append(moves[step])
        for num,elem in enumerate(lista):
            choice = lista[num]
            for subel in lista:
                if subel != choice: 
                    x = (subel[0]+choice[0])/2
                    y = (subel[1]+choice[1])/2
                    if [x,y] in lista:
                        return "A"
        for num,elem in enumerate(listb):
            choice = listb[num]
            for subel in listb:
                if subel != choice:
                    x = (subel[0]+choice[0])/2
                    y = (subel[1]+choice[1])/2
                    if [x,y] in listb:
                        return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"

# 作者：SKYWOW
# 链接：https://leetcode.cn/problems/find-winner-on-a-tic-tac-toe-game/solutions/52568/pythonjing-zi-qi-by-skywow/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。