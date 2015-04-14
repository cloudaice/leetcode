#-*- coding: utf-8 -*-

import math


class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]
        l = self.grayCode(n - 1)
        bigger = int(math.pow(2, n - 1))
        l1 = [i + bigger for i in l]
        l1.reverse()
        return l + l1

if __name__ == "__main__":
    s = Solution()
    print s.grayCode(2)
