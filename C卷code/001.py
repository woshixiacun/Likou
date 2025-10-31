# from typing import List

n, k = map(int, input().split())

def game(n: int, k: int):
    visited = [False] * n
    frd, i = 0, 0
    while not visited[frd]: #遍历friend
        visited[frd] = True # 接到过球的人变成true
        i += 1 # 第i个friend
        frd = (frd + i * k) % n #从第 n个朋友的位置开始顺时针移动 1 步会回到第 1个朋友的位置
    ans = []
    for i in range(n):
        if not visited[i]: #如果不是true，记录其位置(实际位置从1 开始)
            ans.append(i + 1)
    return ans

print(game(n, k))