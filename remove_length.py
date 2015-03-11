#-*- coding: utf-8 -*-


class Solution:
    def removeElement(self, A, elem):
        l = len(A)
        s = A[:]
        for item in s:
            if item == elem:
                l -= 1
                A.remove(item)
        return l

if __name__ == "__main__":
    s = Solution()
    A = [3, 3]
    l = s.removeElement(A, 3)
    print A, l
