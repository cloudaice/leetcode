#-*- coding: utf-8 -*-


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        return reduce(lambda a, b: a ^ b, A)


if __name__ == "__main__":
    s = Solution()
    print s.singleNumber([1, 2, 1])
