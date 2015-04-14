#-*- coding: utf8 -*-


class Solution:
    def maxSubArray(self, A):
        rst = 0
        if len(A) == 0:
            return rst
        rst = A[0]
        val = 0

        for item in A:
            val += item
            if val < 0:
                rst = max(rst, val)
                val = 0
            else:
                rst = max(rst, val)
        return rst


if __name__ == "__main__":
    s = Solution()
    print s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
