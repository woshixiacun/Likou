
class Solution:
    def isPalindrome(self, x: int) -> bool:
        revert = 0
        x0 = x
        while x/10 > 0:
            num = x % 10
            x = x // 10
            revert = revert*10 + int(num)
            # print(num,x,revert)

        if revert == x0:
            return True
        else:
            return False


x = 2
a = Solution().isPalindrome(x)
print(a)