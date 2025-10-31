# 输入获取
# arr = list(map(int, input().split(",")))
arr = [1,-5,-6,4,7,2,-2]

# 算法入口
def getResult():
    n = len(arr)

    dp = [0] * n #存放每一轮的score

    for i in range(n):
        if i == 0:
            dp[0] = max(0, arr[0])
        elif i < 3:
            dp[i] = max(0, dp[i - 1] + arr[i]) #总得分等于上一次翻牌总得分+当前牌的数字
        else:
            dp[i] = max(dp[i - 3], dp[i - 1] + arr[i])

    return dp[-1]


# 算法调用
print(getResult())