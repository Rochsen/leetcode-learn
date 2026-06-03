#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#


# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 创建默认值为 list 的字典
        anagram_map = defaultdict(list)

        for s in strs:
            # 核心思路：异位词排序后是一样的，例如 "eat" -> "aet", "tea" -> "aet"
            # 将排序后的字符元组作为 Key (元组比字符串更适合作为字典键，且不可变)
            key = tuple(sorted(s))
            print(f"key = {key}")

            # 将原始字符串添加到对应 Key 的列表中
            anagram_map[key].append(s)

            print(f"anagram_map = {anagram_map}")

        # 返回字典中所有的值（即分组后的列表）
        return list(anagram_map.values())

# @lc code=end


if __name__ == "__main__":
    sol = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    a = sol.groupAnagrams(strs)

    print(a)
