# 输入获取
n = 6#int(input())
arr = [10, 20, 30, 15, 23, 12]#list(map(int, input().split()))
m = 3#int(input())


# 算法入口
def getResult():
    sumV = sum(arr[:m]) # 前三个值的和
    ans = sumV

    for i in range(1, n-m+1):
        sumV += arr[i+m-1] - arr[i-1] #加后一个，减前一个
        ans = max(ans, sumV)

    return ans


# 算法调用
print(getResult())