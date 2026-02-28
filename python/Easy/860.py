"""
860. 柠檬水找零

在柠檬水摊上，每一杯柠檬水的售价为 5 美元。顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
"""


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for b in bills:
            if b == 5:  # 无需找零
                five += 1
            elif b == 10:  # 返还 5
                five -= 1
                ten += 1
            elif ten > 0:  # 此时 b=20，优先用 10 美元，返还 10+5
                five -= 1
                ten -= 1
            else:  # 此时 b=20，返还 5+5+5
                five -= 3
            if five < 0:  # 无法正确找零
                return False
        return True
    
        # five = 0
        # ten = 0
        # for b in bills:
        #     if b == 5:
        #         five += 1
        #     elif b == 10:
        #         ten += 1
        #         five -= 1
        #         if five < 0:
        #             return False
        #     else:
        #         if ten > 0 and five > 0:
        #             ten -= 1
        #             five -= 1
        #         elif five >= 3:
        #             five -= 3
        #         else:
        #             return False 
        # return True