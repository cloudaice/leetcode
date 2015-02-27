#-*- coding: utf-8 -*-


class Solution:
    def threeSumClosest(self, num, target):
        num.sort()
        muti = 100000000
        for i in range(len(num)):
            l = num[i + 1:]
            diff = self.twoSumClosest(l, target - num[i])
            if abs(diff) < abs(muti):
                muti = diff

        return target + muti
    
    def twoSumClosest(self, num, target):
        muti = 1000000000
        i = 0
        j = len(num) - 1
        while i < j:
            diff = num[i] + num[j] - target
            if abs(diff) < abs(muti):
                muti = diff
            if diff < 0:
                i += 1
            elif diff > 0:
                j -= 1
            else:
                return 0
        return muti


if __name__ == "__main__":
    s = Solution()
    print s.threeSumClosest([1, 1, -1, -1, 3], -1)
