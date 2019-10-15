"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        min_index = 0
        indic = {}
        for i, v in enumerate(s):
            if v in indic:
                min_index1 = indic[v] + 1  # 临时记录最后删除位置
                for j in s[min_index:min_index1]:
                    indic.pop(j)
                min_index = min_index1  # 最后位置要推前一位
                indic[v] = i
            else:
                indic[v] = i
                if len(indic) > max:  # 更新最大值
                    max = len(indic)
        return max


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
