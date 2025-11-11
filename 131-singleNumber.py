from collections import defaultdict
class Solution:
    def singleNumber(self, nums) -> int:
        res_dic = defaultdict(list)
        
        for num in nums:
            res_dic[num].append(num)
        # print(res_dic)
        for val in res_dic.values():
            if len(val)==1:
                return val[0]
        

x = [2,2,1]
a = Solution().singleNumber(x)
print(a)