class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        if n ==2:
            return 2
        if n >=3:
            f1 = 1
            f2 = 2
            for  i in range (n-2):
                ori_f2 = f2
                f2 = f1+f2
                f1 = ori_f2
        return f2



s =4
a = Solution().climbStairs(s)

print(a)