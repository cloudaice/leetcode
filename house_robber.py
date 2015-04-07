#-*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.fn = {}

    def rob(self, num):
        l = len(num)
        if l in self.fn:
            return self.fn[l]
        if l == 0:
            self.fn[l] = 0
        elif l == 1:
            self.fn[l] = num[0]
        elif l == 2:
            self.fn[l] = max(num[0], num[1])
        else:
            self.fn[l] = max(num[0] + self.rob(num[2:]), num[1] + self.rob(num[3:]))
        return self.fn[l]


if __name__ == "__main__":
    s = Solution()
    print s.rob([2, 3, 4, 5, 6])
