#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希映射，存储字符到其最新索引的映射
        char_index_map = {}
        
        # 左指针，表示当前无重复子串的起始位置
        left = 0
        
        # 记录最大长度
        max_len = 0
        
        # 右指针遍历字符串
        for right in range(len(s)):
            current_char = s[right]
            
            # 如果当前字符已经在映射中，并且其上次出现的位置在左指针右侧（即在当前窗口内）
            if current_char in char_index_map and char_index_map[current_char] >= left:
                # 将左指针移动到重复字符上次出现位置的下一位
                left = char_index_map[current_char] + 1
            
            # 更新当前字符的最新索引
            char_index_map[current_char] = right
            
            # 计算当前窗口长度，并更新最大长度
            # 当前窗口长度为 right - left + 1
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                
        return max_len
# @lc code=end


if __name__ == '__main__':
    sol = Solution()
    
    # 测试用例
    t1 = sol.lengthOfLongestSubstring("abcabcbb")
    print(f"abcabcbb: {t1}") # 期望输出: 3 ("abc")

    t2 = sol.lengthOfLongestSubstring("bbbbb")
    print(f"bbbbb: {t2}")     # 期望输出: 1 ("b")

    t3 = sol.lengthOfLongestSubstring("pwwkew")
    print(f"pwwkew: {t3}")    # 期望输出: 3 ("wke")

    t4 = sol.lengthOfLongestSubstring("au")
    print(f"au: {t4}")        # 期望输出: 2 ("au")

    t5 = sol.lengthOfLongestSubstring("dvdf")
    print(f"dvdf: {t5}")      # 期望输出: 3 ("vdf")
    
    t6 = sol.lengthOfLongestSubstring("")
    print(f"empty: {t6}")     # 期望输出: 0