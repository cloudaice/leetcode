#-*- coding: utf-8 -*-

# 属于最简单的动态规划, 计算出从左上角到每一个格子的最短距离，知道计算到右下角的格子


class Solution():
    def minPathSum(slef, grid):
        dic = {}
        m, n = 0, 0
        n = len(grid)
        m = len(grid[0]) if n != 0 else 0
        if m * n == 0:
            return 0
        dic[(0, 0)] = grid[0][0]
        for i in range(1, n):
            dic[(i, 0)] = dic[(i - 1, 0)] + grid[i][0]
        for i in range(1, m):
            dic[(0, i)] = dic[(0, i - 1)] + grid[0][i]

        for i in range(1, n):
            for j in range(1, m):
                target = min(dic[(i - 1, j)], dic[(i, j - 1)])
                dic[(i, j)] = target + grid[i][j]
        return dic[(n - 1, m - 1)]

if __name__ == "__main__":
    s = Solution()
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print s.minPathSum(grid)
