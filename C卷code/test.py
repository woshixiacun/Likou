from collections import deque

st = "abcd"
list1 = [0, 1, 2, 3]
dst = deque(st)
dlist1 = deque(list1)

# 从后面添加
dst.append(4)
dlist1.append("k")

dst.appendleft(4)
dlist1.appendleft("k")

a = dst.pop()
b = dst.popleft()

# count()
# 统计队列中的元素个数（与list同）
nums = dst.count('a')

dst.clear()
# print(dst)
# print(dlist1)



# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。

# 示例 1：

# 输入：s = "(())"   （（（   ）））)

# 输出：true
s = "((())))" 
# s = "]"
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    res = []

    for str in s:
        if str == '(':
            res.append(')')
        elif str == '[':
            res.append(']')
        elif str == '{':
            res.append('}')
        else:
            if res != []:
                a = res.pop()
                if a == str:
                    continue
                else:
                    return False
            else:
                return False
    
    if res == []:
        return True
    return False
    
print(isValid(s))

s = "(())(]"   

def isValid2(s) -> bool:
    if len(s) % 2 == 1:
        return False
    
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = list()
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    
    return not stack

print(isValid2(s))
    
        