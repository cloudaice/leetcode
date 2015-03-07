#-*- coding: utf-8 -*-


class Solution:
    def searchInsert(self, A, target):
        left = 0
        right = len(A) - 1
        return self.binarySearch(A, left, right, target)

    def binarySearch(self, A, i, j, target):
        mid = (i + j) / 2
        if A[mid] == target:
            return mid
        if i == j:
            if A[mid] > target:
                return mid
            else:
                return mid + 1
        if A[mid] < target:
            return self.binarySearch(A, mid + 1, j, target)
        else:
            if mid == i:
                return mid
            return self.binarySearch(A, i, mid - 1, target)

if __name__ == "__main__":
    s = Solution()
    print s.searchInsert([1, 3], 0)
