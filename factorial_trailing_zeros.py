#-*- coding: utf-8 -*-


class Solution:
    def trailingZeroes(self, n):
        rst = 0
        while n / 5 != 0:
            n = n / 5
            rst += n
        return rst

if __name__ == "__main__":
    s = Solution()
    print s.trailingZeroes(100)
