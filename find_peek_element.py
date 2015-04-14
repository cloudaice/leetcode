#-*- coding: utf-8 -*-


class Solution:
    def findPeekElement(self, num):
        l = len(num)
        for i in range(l):
            if i - 1 >= 0 and i + 1 <= l - 1:
                if num[i] > num[i - 1] and num[i] > num[i + 1]:
                    return i
            elif i - 1 >= 0:
                if num[i] > num[i - 1]:
                    return i
            elif i + 1 <= l - 1:
                if num[i] > num[i + 1]:
                    return i
            else:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.findPeekElement([1, 2, 3, 1])
