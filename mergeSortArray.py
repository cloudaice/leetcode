#-*- coding: utf-8 -*-


# 这题比较恶心，case里提供的A，len(A) == m + n, 而不是len(A) == m


class Solution:
    def merge(self, A, m, B, n):
        i = 0
        for j, item in enumerate(B):
            while i < m + j and A[i] < item:
                i += 1
            A.insert(i, item)


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [2, 5, 6]
    s = Solution()
    s.merge(a, 3, b, 3)
    print a
