from typing import List
from copy import deepcopy

class Solution:
    def __init__(self):
        self.direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 4个方向
    # 计算每个格子的着火时间
    def bfsFireTime(self, grid):
        fireTime = [[int(1e9)] * self.n for _ in range(self.m)]
        graph = deepcopy(grid)
        q = []
        for i in range(self.m):
            for j in range(self.n):
                if graph[i][j] == 1:
                    q.append((i, j)) # 着火的坐标放入队列
                    fireTime[i][j] = 0 # 设置初始时间0
        # bfs算法求着火的时间
        while q: 
            x, y = q[0]
            q = q[1:]
            for dx, dy in self.direction:
                tx, ty = x + dx, y + dy # 检查其相邻的单元格
                # 处理边界值，并且该格子没有着火（=0）
                if tx >= 0 and tx < self.m and ty >= 0 and ty < self.n and not graph[tx][ty]: 
                    # 将新的着的格子加入队列
                    q.append((tx, ty)) 
                    # 并更新fireTime和graph
                    fireTime[tx][ty] = fireTime[x][y] + 1  
                    graph[tx][ty] = 1 # 变成着火
        self.fireTime = fireTime
    
    def check(self, grid, t):
        peopleTime = [[0] * self.n for _ in range(self.m)] # 存储人到达每个单元格的时间。初始值设为0。
        graph = deepcopy(grid)
        q = []
        q.append((0, 0))
        graph[0][0] = 2 # 起点
        peopleTime[0][0] = t # 初始时间
        # bfs算法求人到达格子的时间
        while q: 
            x, y = q[0]
            q = q[1:]
            thisTime = peopleTime[x][y] + 1
            for dx, dy in self.direction:
                tx, ty = x + dx, y + dy
                if tx >= 0 and tx < self.m and ty >= 0 and ty < self.n and not graph[tx][ty]:
                    graph[tx][ty] = 2
                    if tx == self.m - 1 and ty == self.n - 1 and thisTime <= self.fireTime[-1][-1]:
                        return True
                    if thisTime < self.fireTime[tx][ty]: # 到达时间小于着火时间
                        # 更新peopleTime并将其加入队列
                        peopleTime[tx][ty] = thisTime 
                        q.append((tx, ty))
        return False

    def maxTime(self, grid):
        self.m, self.n = len(grid), len(grid[0])
        self.bfsFireTime(grid)
        l, r = 0, self.m * self.n
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if self.check(grid, mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return int(1e9) if ans >= self.m * self.n else ans

grid = [[0,2,0,0,0,0,0],
        [0,0,0,2,2,1,0],
        [0,2,0,0,1,2,0],
        [0,0,2,2,2,0,2],
        [0,0,0,0,0,0,0]]

print(Solution().maxTime(grid))

"""
[[6, ∞, 4, 3, 2, 1, 2],
    [5, 4, 3, ∞, ∞, 0, 1],
    [6, ∞, 2, 1, 0, ∞, 2],
    [7, 8, ∞, ∞, ∞, 14, ∞],
    [8, 9, 10, 11, 12, 13, 14]]
"""
