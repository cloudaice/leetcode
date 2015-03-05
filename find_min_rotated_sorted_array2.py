#-*- coding: utf-8 -*-


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if len(num) <= 3:
            return min(num)
        if num[0] < num[-1]:
            return num[0]
        mid = len(num) / 2
        if num[mid] > num[0]:
            return self.findMin(num[mid + 1:])
        elif num[mid] < num[0]:
            return self.findMin(num[1:mid + 1])
        else:
            return min(self.findMin(num[:mid]), self.findMin(num[mid + 1:]))

if __name__ == "__main__":
    s = Solution()
    print s.findMin([2, 1])
