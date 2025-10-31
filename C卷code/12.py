n,m = list(map(int,input().split()))
F,T=[],[]
for i in range(n):
    f = int(input())
    F.append(f)

for i in range(m):
    t = list(map(int,input().split()))
    T.append(t)


# 算法入口
def getResult():
    T_F = []
    for id_t,t in enumerate(T):
        sum = 0
        for id_f in t:
            sum += F[id_f-1]
        T_F.append([sum,id_t+1])

    T_F.sort(key=lambda x: (x[0]), reverse=True)


    return " ".join(map(lambda x: str(x[1]), T_F))


# 算法调用
print(getResult())


# # 输入获取
# n, m = map(int, input().split())

# features = [0] * (n + 1)
# for i in range(1, n+1):
#     features[i] = int(input())

# cases = []
# for i in range(1, m+1):
#     priority = sum(map(lambda x: features[int(x)], input().split()))
#     cases.append([priority, i])

# cases.sort(key=lambda x: (-x[0], x[1]))

# for _, idx in cases:
#     print(idx)