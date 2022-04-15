import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        visited = set()
        ans = 0
        
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                ro, co = q.pop()
                direc = [[-1,0],[1,0],[0,1],[0,-1]]
                for dr, dc in direc:
                    rn, cn = ro + dr, co +dc
                    if (rn in range(row) and
                        cn in range(col) and
                        grid[rn][cn] == '1' and
                        (rn, cn) not in visited):
                        q.append((rn, cn))
                        visited.add((rn, cn))   
            return
        
        for r in range(row):
            for c in range(col):
                if ((r,c) not in visited) and (grid[r][c] == '1'):
                    bfs(r,c)
                    ans += 1
        return ans
