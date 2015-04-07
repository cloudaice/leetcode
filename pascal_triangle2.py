#-*- coding: utf-8 -*-


class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        last = self.getRow(rowIndex - 1)
        return map(lambda x, y: x + y, [0] + last, last + [0])


if __name__ == "__main__":
    s = Solution()
    print s.getRow(4)
