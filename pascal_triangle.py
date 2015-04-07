#-*- coding: utf-8 -*-


class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            rst = self.generate(numRows - 1)
            last = rst[-1]
            net = map(lambda x, y: x + y, [0] + last, last + [0])
            rst.append(net)
            return rst


if __name__ == "__main__":
    s = Solution()
    print s.generate(5)
