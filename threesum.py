#-*- coding: utf-8 -*-


class Solution:
    def threeSum(self, num):
        results = []
        if len(num) < 3:
            return results
        num.sort()
        for i in range(len(num)):
            l = num[i + 1:]
            r = self.twoSum(l, 0 - num[i])
            results += [[num[i]] + item for item in r]
        m = {}
        result = []
        for item in results:
            if tuple(item) in m:
                continue
            result.append(item)
            m[tuple(item)] = 1
        return result

    def twoSum(self, num, target):
        results = []
        i = 0
        j = len(num) - 1
        while i < j:
            diff = num[i] + num[j] - target
            if diff > 0:
                j -= 1
            elif diff < 0:
                i += 1
            else:
                results.append([num[i], num[j]])
                i += 1
                j -= 1

        return results

if __name__ == "__main__":
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1, -4])
