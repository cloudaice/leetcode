#-*- coding: utf-8 -*-


class Solution:
    def hammingWeight(self, n):
        num = 0
        for i in range(32):
            bit = n & 1
            if bit == 1:
                num += 1
            n = n >> 1
        return num


if __name__ == "__main__":
    s = Solution()
    print s.hammingWeight(11)
