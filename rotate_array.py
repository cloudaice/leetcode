#-*- coding: utf-8 -*-


class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, 3)
    print nums
