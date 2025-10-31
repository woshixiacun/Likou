mtrx = []
n  = int(input())
for i in range(n):
    row = list(map(int, input().split()))
    mtrx.append(row)
# print(mtrx)

def minDownPath(matrix):
    dp = [matrix[0]]
    for i in range(1, n):
        cur_min = [0] * n #当前行和最小下降路径
        for j in range(n):
            mn = dp[-1][j] #上一行，3个元素
            if j > 0: # 从第2列~最后一列（边界另外处理）
                mn = min(mn, dp[-1][j - 1])
            if j < n - 1: #第1列~倒数第2列
                mn = min(mn, dp[-1][j + 1])
            cur_min[j] = mn + matrix[i][j] #上一行min+当前元素
        dp.append(cur_min)
    return min(dp[-1])

print(minDownPath(mtrx))


def minDownPath2(matrix):
    dp = [matrix[0]]
    for i in range(1, n):
        cur_min = [0] * n #当前行和最小下降路径
        for j in range(n):
            if j == 0:
                cur_min[j] = min(dp[-1][j], dp[-1][j+1])
            elif j == n-1:
                cur_min[j] = min(dp[-1][j], dp[-1][j-1])
            else:
                cur_min[j] = min(dp[-1][j], dp[-1][j-1], dp[-1][j+1])
        dp.append(cur_min)
    return min(dp[-1])
