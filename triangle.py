#-*- coding: utf-8 -*-


class Solution:
    def minimumTotal(self, triangle):
        if triangle == []:
            return 0
        fn = triangle[-1]
        dep = len(triangle) - 2
        while dep >= 0:
            for idx, item in enumerate(triangle[dep]):
                fn[idx] = min(fn[idx], fn[idx + 1]) + item
            dep = dep - 1
        return fn[0]


if __name__ == "__main__":
    s = Solution()
    t = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print s.minimumTotal(t)
