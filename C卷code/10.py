# inp = '(1+(2+3)*(3+(8+0))+1-2))'

# bowl =[]
# cnt_l = 0
# cnt_r = 0
# for i in inp:
#     if i == '(':
#         bowl.append(i)
#         cnt_l+=1
#     if i == ')':
#         bowl.append(i)
#         cnt_r+=1 

# if cnt_l == cnt_r:
#     print(cnt_l)
# else:
#     print('error')


# 输入获取
# s =  input() #')(1+(2+3)*(3+(8+0))+1-2)('
s = '((( )))' #')(1+(2+3)*(3+(8+0))+1-2)('


# 算法入口
def getResult(s):
    count = 0

    stack = []
    for c in s:
        if c != '(' and c != ')':
            continue
        
        if len(stack) > 0 and c == ')':
            if stack[-1] == '(':
                stack.pop()
                count += 1
                continue
            return -1

        stack.append(c)

    if len(stack) > 0:
        return -1

    return count


# 算法调用
print(getResult(s))