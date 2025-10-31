# 输入获取
m = 3#int(input()) 


## 递归
def recursive(arr, m, count):
    nxt = []

    for v in arr:
        if count == m + 1:
            count = 1

        if count % m != 0:
            nxt.append(v)

        count += 1

    if len(nxt) >= m:
        return recursive(nxt, m, count)
    else:
        return ",".join(map(str, nxt))


# 算法入口
def getResult():
    if m <= 1 or m >= 100:  #3
        return "ERROR!"

    arr = [i for i in range(1, 101)]

    return recursive(arr, m, 1)


# 算法调用
print(getResult())