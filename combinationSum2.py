#-*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.m = {}
        self.num = []

    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.num = candidates[:]
        r = self.generate(0, target)
        if r is None:
            return []
        result = []
        m = {}
        for item in r:
            if tuple(item) in m:
                continue
            m[(tuple(item))] = 1
            result.append(item)
        return result
    
    def generate(self, i, target):
        result = None
        if target == 0:
            return [[]]
        if i > len(self.num) - 1:
            return None
        if self.num[i] > target:
            return None
        elif self.num[i] < target:
            if (i, target) not in self.m:
                j = i
                while j < len(self.num):
                    sub = self.join(self.num[j], self.generate(j + 1, target - self.num[j]))
                    result = self.union(result, sub)
                    j += 1
                self.m[(i, target)] = result
            return self.m[(i, target)]
        else:
            return [[self.num[i]]]
    
    def join(self, a, l):
        if l is None:
            return None
        return [[a] + item for item in l]

    def union(self, l1, l2):
        if l1 and l2:
            return l1 + l2
        return l1 or l2


if __name__ == "__main__":
    s = Solution()
    print s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
