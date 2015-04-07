#-*- coding: utf-8 -*-


class Solution:
    def reverseBits(self, n):
        rst = 0
        for i in range(32):
            rst = rst << 1
            if n & 1 == 1:
                rst += 1
            n = n >> 1
        return rst

if __name__ == "__main__":
    s = Solution()
    print s.reverseBits(43261596)
