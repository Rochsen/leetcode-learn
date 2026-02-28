"""
1232. 缀点成线
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        else:
            div_part = coordinates[0][0] - coordinates[1][0]
            if div_part == 0:
                k = float(inf)
            else:
                k = (coordinates[0][1] - coordinates[1][1]) / div_part

            for idx in range(1, len(coordinates)- 1):
                div_part = coordinates[idx][0] - coordinates[idx+1][0]
                if div_part == 0:
                    tmp_k = float(inf)
                else:
                    tmp_k = (coordinates[idx][1] - coordinates[idx+1][1]) / div_part
                    
                if k != tmp_k:
                    return False
            
            return True