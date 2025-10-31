# 输入获取
s = input()

# 全局变量
stack = []
topRepeat = 0
isEng = False

dictionary = (" ", ",.", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")


# 基于dictionary，获取一个数字c被重复repeat次后，对应的字符
def mapping(c, repeat):
    num = int(c)
    s1 = dictionary[num]
    i = (repeat - 1) % len(s1)
    return s1[i]


# 英文模式连续按同一个按键会依次出现这个按键上的字母，如果输入”/”或者其他字符，则循环中断
# interrupt用于处理循环中断后的逻辑
def interrupt():
    global topRepeat
    if not isEng or len(stack) == 0 or topRepeat == 0:
        return
    stack.append(mapping(stack.pop(), topRepeat))
    topRepeat = 0


# 算法入口
def getResult():
    global s
    global isEng
    global topRepeat

    s += " "

    for c in s:
        if c == '#':
            # 如果输入”/”或者其他字符，则循环中断
            interrupt()
            # #用于切换模式
            isEng = not isEng
        elif c == '/':
            # 如果输入”/”或者其他字符，则循环中断
            interrupt()
        else:
            # 数字模式直接输出数字
            if not isEng:
                stack.append(c)
                continue

            # 英文模式，需要检查栈顶
            # 如果栈顶不是英文模式字符（这里可以基于topRepeat判断，topRepeat是英文模式下对应按键的重复次数，如果为0，则说明栈顶存储的不是英文模式字符），则缓存对应字符c，并记录重复次数
            if topRepeat == 0:
                stack.append(c)
                topRepeat += 1
                continue

            # 如果栈顶字符有重复次数，则此时需要比较当前按键c和之前重复的按键stack.getLast是否相同
            if c != stack[-1]:
                # 如果输入”/”或者其他字符，则循环中断
                interrupt()
                stack.append(c)

            topRepeat += 1

    return "".join(stack[:-1])


# 算法调用
print(getResult())