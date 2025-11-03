'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        harshtable = dict()
        s_out = ''
        for id,x in enumerate(s):
            s_out = s_out + x
            print(s_out)
            harshtable[s[id+1:]] = s_out
                
            print(harshtable)

        return 1



s = "abcabcbb"
a = Solution().lengthOfLongestSubstring(s)


