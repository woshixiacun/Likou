'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：
-0
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
'''
nums = [0,1,1,2]

num_set = set(nums) #去重

def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = set(nums) #去重
    if len(nums)==1:
        return 1
    if len(nums)==0:
        return 0
    else:
        
        num_set = sorted(nums)
        count=1
        count_list=[]
        
        for i in range(len(num_set)-1):
            num=num_set[i]
            if num+1==num_set[i+1]:
                count+=1
                count_list.append(count)
            else:
                count=1
                count_list.append(count)
                continue
        return max(count_list)
    
print(longestConsecutive)