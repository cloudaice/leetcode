#-*- coding: utf-8 -*-


class Solution:
    def sortColors(self, A):
        # i 第一个1的下标
        # j 从左往右的游标
        i, j = -1, 0
        # k 从右往左的游标
        k = len(A) - 1

        while j <= k:
            if A[j] == 1 and i == -1:
                i = j
                j += 1
            elif A[j] == 0 and i != -1:
                A[i], A[j] = A[j], A[i]
                i += 1
                j += 1
            elif A[j] == 2:
                if A[k] != 2:
                    A[j], A[k] = A[k], A[j]
                    k -= 1
                else:
                    k -= 1
            else:
                j += 1


if __name__ == "__main__":
    s = Solution()
    A = [1, 0]
    s.sortColors(A)
    print A
