# -*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.m = {}

    # @return an integer
    def numTrees(self, n):
        if n <= 1:
            return 1
        s = 0
        for i in range(0, n):
            a = self.m[i] if i in self.m else self.numTrees(i)
            self.m[i] = a
            idx = n - i - 1
            b = self.m[idx] if idx in self.m else self.numTrees(idx)
            self.m[n - i - 1] = b
            s += a * b
        self.m[n] = s
        return s


if __name__ == "__main__":
    s = Solution()
    print s.numTrees(4)
