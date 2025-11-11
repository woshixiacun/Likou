class Solution:
    def reverse(self, x: int) -> int:
        num_list = []
        for i in str(x):
            num_list.append(i)
        if num_list[0] == '-':
            num_list = num_list[1:][::-1]
            num = -int(''.join(num_list))
        else:
            num_list = num_list[::-1]
            num = int(''.join(num_list))
        if num < -2**31 or num > 2**31-1:
            return 0
        return num
            


x = 123
a = Solution().reverse(x)
print(a)