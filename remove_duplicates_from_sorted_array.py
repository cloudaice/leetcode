#-*- coding: utf-8 -*-


class Solution:
    def removeDuplicates(self, A):
        if A == []:
            return 0
        tmp = A[0]
        i = 1
        while i < len(A):
            if A[i] == tmp:
                A.remove(tmp)
            else:
                tmp = A[i]
                i += 1
