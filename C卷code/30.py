# #————————————————————————分治递归求解（带缓存优化）——————————————————————————————
# # 输入获取
# n = int(input())

# cache = [-1] * 51
# cache[0] = 0
# cache[1] = 1
# cache[2] = 1
# cache[3] = 2


# # 算法入口
# def recursive(n):
#     if cache[n] != -1:
#         return cache[n]

#     cache[n] = recursive(n - 1) + recursive(n - 3)
#     return cache[n]


# # 调用算法
# print(recursive(n))



#————————————————————————动态规划算法求解——————————————————————————————
# 输入获取
n = 50#int(input())


# 算法入口
def getResult():
    dp = [0]*(n+1)

    if n >= 1:
        dp[1] = 1 #1层 有一种上法，每次1阶
    if n >= 2:
        dp[2] = 1 #2层 有一种上法，每次1阶
    if n >= 3:
        dp[3] = 2 #3层以上 有2种上法，每次1阶or2阶-

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3] #第i层可以从i-层 一步上，or 从i-3层一步上

    return dp[n]


# 调用算法
print(getResult())