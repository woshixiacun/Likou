# 输入获取
s = 'XXYYXY' #input()


# 算法入口
def getResult():
    countX = 0
    countY = 0

    ans = 0

    for c in s:
        if c == 'X':
            countX += 1
        else:
            countY += 1

        if countX == countY:
            ans += 1

    return ans


# 算法调用
print(getResult())