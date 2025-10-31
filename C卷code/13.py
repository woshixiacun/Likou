# L = [0, 0, 100, 2, 2, 99, 0 ,2]#[0,1,2,3,4]
# M= 2
# aves=[]
# max = 0
# for idi, i in enumerate(L):
#     sum=i
    
#     for idj, j in enumerate(L):
#         if idj <= idi:
#             continue
#         sum+=j
#         ave=sum/(idj-idi+1)
#         if ave<= M  and (idj-idi+1) > max:
#             max = (idj-idi+1)
#             aves=[]
#             aves.append([idi, idj])
#         elif ave<=M  and (idj-idi+1) == max:
#             max = (idj-idi+1)
#             aves.append([idi, idj])
            

# print(aves)


# 输入获取
minAverageLost = int(input())
nums = list(map(int, input().split()))


# 算法入口
def getResult():
    n = len(nums)

    preSum = [0] * (n + 1)
    for i in range(1, n + 1):
        preSum[i] = preSum[i - 1] + nums[i - 1]

    ans = []
    maxLen = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            # sumV 是 区间 [i, j-1] 的和
            sumV = preSum[j] - preSum[i]
            length = j - i
            lost = length * minAverageLost

            if sumV <= lost:
                if length > maxLen:
                    ans = [[i, j - 1]]
                    maxLen = length
                elif length == maxLen:
                    ans.append([i, j - 1])

    ans.sort(key=lambda x: x[0])

    if len(ans) == 0:
        return "NULL"
    else:
        return " ".join(map(lambda x: "-".join(map(str, x)), ans))


# 算法调用
print(getResult())