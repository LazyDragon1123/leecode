from importlib.resources import path


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if (len(obstacleGrid[0]) == 1) or (len(obstacleGrid) == 1):
            for arr in obstacleGrid:
                if 1 in arr:
                    return 0
            return 1
        if obstacleGrid[0][0] == 1:
            return 0
        paths = [[0]* (len(obstacleGrid[0]) + 1) for _ in range(len(obstacleGrid) + 1)]
        banned = []
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    banned.append([i+1,j+1])
        print(banned)
        paths[1][1] = 1
        for i in range(1, len(obstacleGrid)+1):
            for j in range(1, len(obstacleGrid[0]) + 1):
                if [i,j] == [1,1]:
                    continue
                if [i,j] in banned:
                    paths[i][j] = 0
                    print(paths[i][j])
                    continue
                paths[i][j] = paths[i -1][j] + paths[i][j-1]
                print(paths[i][j])
                continue
        return paths[len(obstacleGrid)][len(obstacleGrid[0])]
