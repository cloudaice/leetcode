#-*- conding: utf-8 -*-


class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        m = {}
        candidates.sort()
        
        def fn(l, target):
            if target == 0:
                return [[]]
            if l is None or l[0] > target:
                return None
            if l[0] == target:
                return [[l[0]]]
            if (l[0], target) in m:
                return m[(l[0], target)]

            sum = []
            for i in range(len(l)):
                prefix = l[i]
                #print prefix, l[i:], target - prefix
                tmp = fn(l[i:], target - prefix)
                m[(prefix, target - target - prefix)] = tmp
                ns = join(prefix, tmp)
                if ns is not None:
                    sum += ns
            if len(sum) == 0:
                sum = None

            m[(l[0], target)] = sum
            return sum
        
        def join(n, l):
            if l is None:
                return None
            return [[n] + item for item in l if item is not None]

        result = fn(candidates, target)
        if result is None:
            return []
        return result

if __name__ == "__main__":
    o = Solution()
    print o.combinationSum([21, 46, 35, 20, 44, 31, 29, 23, 45, 37, 33, 34, 39, 42, 24, 40, 41, 26, 22, 38, 36, 27, 25, 49, 48, 43], 71)
    print o.combinationSum([2], 1)
