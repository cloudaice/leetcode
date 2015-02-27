#-*- coding: utf-8 -*-


class Solution:
    def fourSum(self, num, target):
        result = []
        if len(num) < 4:
            return result
        num.sort()
        for i in range(len(num)):
            l = num[i + 1:]
            r = self.threeSum(l, target - num[i])
            result += [[num[i]] + item for item in r]
        m = {}
        results = []
        for item in result:
            if tuple(item) in m:
                continue
            results.append(item)
            m[tuple(item)] = 1
        return results

    def threeSum(self, num, target):
        result = []
        for i in range(len(num)):
            l = num[i + 1:]
            r = self.twoSum(l, target - num[i])
            result += [[num[i]] + item for item in r]
        return result

    def twoSum(self, num, target):
        result = []
        i = 0
        j = len(num) - 1
        while i < j:
            diff = num[i] + num[j] - target
            if diff > 0:
                j -= 1
            elif diff < 0:
                i += 1
            else:
                result.append([num[i], num[j]])
                i += 1
                j -= 1
        return result

if __name__ == "__main__":
    s = Solution()
    print s.fourSum([1, 0, -1, 0, -2, 2], 0)
