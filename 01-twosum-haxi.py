from typing import List
nums = [2,11,15,7]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        harshtable = dict()
        for id, num in enumerate(nums): # 查 target - num 这个对象本身是不是 键（key）
            if target - num in harshtable:
                return [id, harshtable[target - num]]
            harshtable[nums[id]] = id
        return []

    
a = Solution().twoSum(nums,target)   

print(a)      