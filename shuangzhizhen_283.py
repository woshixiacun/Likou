
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
 

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]
 
'''
nums = [0,1,0,3,12]

def moveZeroes(nums):
    new_nums=[]
    count_zero=0
    for i in nums:
        if i==0:
            count_zero+=1
        else:
            new_nums.append(i)
    new_nums.extend([0]*count_zero)
    return new_nums

a=moveZeroes(nums)
print(a)

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums=[]
        count_zero=0
        for i in nums:
            if i==0:
                count_zero+=1
            else:
                new_nums.append(i)
        new_nums.extend([0]*count_zero)
        nums = new_nums
        return nums
sol = Solution()

print(sol.moveZeroes(nums))

nums = [0,1,0,3,12]
def moveZeroes2(nums):
    left = right = 0
    n = len(nums)
    while right <  n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right +=1 
