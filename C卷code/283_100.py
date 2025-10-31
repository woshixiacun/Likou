
nums = [0,1,0,3,12]
# nums = [0]

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    left = right = 0
    n = len(nums)

    while(right < n):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left = left + 1
        right = right + 1

    print(nums)

moveZeroes(nums)