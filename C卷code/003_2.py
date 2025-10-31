from typing import List
inf = int(1e9)

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fireTime = [[inf] * n for _ in range(m)]

        def bfs(): #求每个格子着火的时间
            q = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        q.append((i, j))
                        fireTime[i][j] = 0
            
            time = 1
            while len(q) > 0:
                tmp = q
                q = []
                for cx, cy in tmp:
                    for nx, ny in (cx, cy - 1), (cx, cy + 1), (cx - 1, cy), (cx + 1, cy):
                        if nx >= 0 and ny >= 0 and nx < m and ny < n:
                            if grid[nx][ny] == 2 or fireTime[nx][ny] != inf:
                                continue
                            q.append((nx, ny))
                            fireTime[nx][ny] = time
                time += 1

        def getArriveTime(stayTime):
            visit = set((0, 0))
            q = []
            q.append((0, 0, stayTime))
            while len(q) > 0:
                tmp = q
                q = []

                for cx, cy, time in tmp:
                    if cx == m - 1 and cy == n - 1:
                        return True
                    for nx, ny in (cx, cy - 1), (cx, cy + 1), (cx - 1, cy), (cx + 1, cy):
                        if nx >= 0 and ny >= 0 and nx < m and ny < n:
                            if (nx, ny) in visit or grid[nx][ny] == 2:
                                continue
                            # 到达安全屋
                            if nx == m - 1 and ny == n - 1:
                                return  time + 1
                            # 火未到达当前位置 
                            if fireTime[nx][ny] > time + 1:
                                q.append((nx, ny, time + 1))
                                visit.add((nx, ny))
            return -1

        # 通过 bfs 求出每个格子的着火时间
        bfs()
        # 找到起点到每个格子的最短路径
        arriveTime = getArriveTime(0)
        # 安全屋不可达
        if arriveTime < 0:
            return -1
        # 火不会到达安全屋 
        if fireTime[m - 1][n - 1] == inf:
            return 10**9
        ans = fireTime[m - 1][n - 1] - arriveTime
        return ans if getArriveTime(ans) >= 0 else ans - 1

grid = [[0,2,0,0,0,0,0],
        [0,0,0,2,2,1,0],
        [0,2,0,0,1,2,0],
        [0,0,2,2,2,0,2],
        [0,0,0,0,0,0,0]]

print(Solution().maximumMinutes(grid))