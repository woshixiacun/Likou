'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
'''
from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        s_out = deque()
        zcy = []
        max_len = j-i
        while j < len(s):
            while s[j] in s_out:
                i+=1
                zcy.append(s_out.popleft())
            max_len = max(max_len,j-i+1)
            s_out.append(s[j])
            
            j+=1
            # print(s_out)

            
        return max_len



s = "abcabcbb"
a = Solution().lengthOfLongestSubstring(s)

print(a)
