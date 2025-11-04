class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        n = len(s)
        start, end = 0, 0          # 记录当前最优的左右边界（左闭右开）

        def expand(l: int, r: int) :
            """从中心 l,r 向左右扩展，返回最终左右边界"""
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1    # 注意循环多走了一步，要缩回来

        for i in range(n):
            # 奇数长度中心
            l1, r1 = expand(i, i)
            # 偶数长度中心
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
            

s = "baabaad"
a = Solution().longestPalindrome(s)
print(a)