# -*- coding: utf-8 -*-


class Solution:
    def majorityElement(self, num):
        count = 0
        result = 0
        for n in num:
            if count == 0 or result == n:
                count += 1
                result = n
            else:
                count -= 1
        return result
