# -*- coding: utf-8 -*-

import math


class Solution:
    def uniquePaths(self, m, n):
        grid = [[1 for i in range(n)] for j in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]


if __name__ == "__main__":
    s = Solution()
    print s.uniquePaths(3, 7)
