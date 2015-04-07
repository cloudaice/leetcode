#-*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.fn = {}

    def climbStairs(self, n):
        if n in self.fn:
            return self.fn[n]

        if n == 0 or n == 1:
            self.fn[n] = 1
        else:
            self.fn[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.fn[n]


if __name__ == "__main__":
    s = Solution()
    print s.climbStairs(100)
