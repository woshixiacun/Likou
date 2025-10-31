from heapq import heappush, heappop
import copy

# 总天数，城市数
T, N = map(int, input().split())
# 路程天数
days = list(map(int, input().split()))

# # 初始化一个大根堆
# heap = list()
# # N个城市的初始金额M和衰减速度D
# for _ in range(N):
#     M, D = map(int, input().split())
#     # 将(M, D)入堆，
#     # 由于维护的是大根堆，所以储存的是(-M, D)
#     heappush(heap, (-M, D))

# # 可以卖唱的总天数X
# X = T - sum(days)

# ans = 0
# # 遍历X天
# for i in range(X):
#     # 如果堆中无元素，则说明所有的城市赚的钱都衰减到0了
#     # 直接退出循环
#     if len(heap) == 0:
#         break
#     # 弹出堆中绝对值最大的M
#     M, D = heappop(heap)
#     # 之前储存的M是负数，改为正数
#     M = -M
#     # 选择在这个城市卖唱，可以赚到M
#     ans += M
#     # 赚完了M，需要衰减D，更新M的值
#     M -= D
#     # 如果M衰减了D之后，仍大于0，说明还有可能继续在这里赚钱，重新入堆
#     if M > 0:
#         heappush(heap, (-M, D))

# print(ans)

last_day = T - sum(days)

# 6

result = []
path = []

# def backtracking(last_day, N):
#     if len(path) == N-1:
#         path.append(last_day)
#         a = copy.deepcopy(path)
#         result.append(a)
#         return
    
#     for i in range(last_day+1):
#         # path.clear()
#         path.append(i)
#         backtracking(last_day-i, N)
#         path.pop()
#         # last_day += i

# backtracking(last_day, N)

for i in range(N):

    for j in range(last_day+1):
        if sum(path) >= last_day:
            break
        if len(path) == N-1:
            path.append(last_day)
            a = copy.deepcopy(path)
            result.append(a)
            path.clear()
            break
        path.append(j)
        break

print(result)
        


# def backtracking(last_day, N, i):

#     if len(path) == N:
#         a = copy.deepcopy(path)
#         result.append(a)
#         return
#     if len(path) == N-1:
#         path.append(last_day)
#         a = copy.deepcopy(path)
#         result.append(a)
#         return
#     path.append(i)
#     backtracking(last_day - i, N, i)


# for i in range(last_day+1):
#     path.clear()
#     backtracking(last_day, N, i)

# print(result)

        
