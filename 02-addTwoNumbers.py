# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""
from collections import deque
l1 = [2,4,3]
l2 = [5,6,4]


from typing import Optional

class Solution:

    def addTwoNumbers(self, l1, l2):
        if len(l1)<len(l2):
            x = l1
            l1 = l2
            l2 = x
        l1 = deque(l1)
        l2 = deque(l2)
        res = []
        flag = 0
        while len(l2) != 0:
            x = l1.pop() + l2.pop() + flag
            if x < 10:
                res.append(x)
                flag = 0
            else:
                res.append(x-10)
                flag = 1
        while len(l1) != 0:
            x = l1.pop() + flag
            if x < 10:
                res.append(x)
                flag = 0
            else:
                res.append(x-10)
                flag = 1
        return list(reversed(res))

            
a = Solution().addTwoNumbers(l1,l2)
print(a)