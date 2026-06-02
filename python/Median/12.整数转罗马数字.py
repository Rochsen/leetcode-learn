#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        dict_roman = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        flag = 0

        res = []

        while num > 0:

            # 获取余数
            last_number = num % 10

            # 拆分 = 位数 * 余数
            tmp_number = last_number * 10**flag

            # 先搜索是否有一样的，如果有直接进入数组, 没有的话就进行计算
            search_res = dict_roman.get(tmp_number, None)

            if search_res:
                res.append(search_res)
            else:
                # 在字典里找不到数字，开始计算
                if 1 < tmp_number < 4:
                    res.append("I" * last_number)
                elif 4 < tmp_number < 9:
                    res.append("V" + "I" * (last_number - 5))
                elif 10 < tmp_number < 40:
                    res.append("X" * last_number)
                elif 40 < tmp_number < 90:
                    res.append("L" + "X" * (last_number - 5))
                elif 100 < tmp_number < 400:
                    res.append("C" * last_number)
                elif 400 < tmp_number < 900:
                    res.append("D" + "C" * (last_number - 5))
                elif 1000 < tmp_number < 4000:
                    res.append("M" * last_number)
                else:
                    pass

            # 获取计算次数
            flag += 1

            # 从后往前推
            num //= 10

        return "".join(res[::-1])


# @lc code=end


if __name__ == "__main__":
    sol = Solution()

    t1 = sol.intToRoman(999)
    print(f"t1: {t1}")

    t2 = sol.intToRoman(3000)
    print(f"t2: {t2}")

    t3 = sol.intToRoman(3749)
    print(f"t3: {t3}")
