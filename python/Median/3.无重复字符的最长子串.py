#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        # 搜索字符的指针
        final_index = 0

        # 不重复的最大长度
        max_len = 1

        while final_index != len(s):
            tmp_max_uls = ""
            for i in range(len(s[final_index: ])):
                if s[final_index+i] not in tmp_max_uls:
                    tmp_max_uls += s[final_index+i]
                else:
                    break

            # 跳出循环后，计算字符数
            tmp_res = len(tmp_max_uls)
            
            # 替换指针位置
            final_index += 1
            
            # 选择更大的那个输出
            max_len = max(max_len, tmp_res)

            print("tmp_max_uls: ", tmp_max_uls)
            print("final_index:", final_index)

        return max_len


if __name__ == '__main__':
    # t1 = Solution().lengthOfLongestSubstring("abcabcbb")
    # print(t1)

    # t2 = Solution().lengthOfLongestSubstring("bbbbb")
    # print(t2)

    # t3 = Solution().lengthOfLongestSubstring("pwwkew")
    # print(t3)

    # t4 = Solution().lengthOfLongestSubstring("au")
    # print(t4)

    t5 = Solution().lengthOfLongestSubstring("dvdf")
    print(t5)

# @lc code=end

