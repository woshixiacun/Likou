# 输入获取
n = 3 #int(input())
k = 3#int(input())
arr = [i + 1 for i in range(n)]

fact = [0] * (n + 1)
fact[1] = 1
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i


# 算法入口  答案
def getResult(n, k, arr):
    if n == 1:
        return "1"

    res = []

    while True:
        prefix = arr[(k - 1) // fact[n-1]]
        res.append(str(prefix))

        k = k % fact[n-1]
        if k == 0:
            k = fact[n-1]

        arr = list(filter(lambda x: x != prefix, arr))
        n -= 1
        if k == 1:
            res.append("".join(map(str, arr)))
            break

    return "".join(res)


# 算法调用
print(getResult(n, k, arr))