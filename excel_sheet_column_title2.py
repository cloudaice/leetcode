#-*- coding: utf-8 -*-


class Solution:
    def titleToNumber(self, s):
        str_num = [ord(i) - ord('A') + 1 for i in s]
        l = len(str_num) - 1
        return sum([n * pow(26, l - i) for i, n in enumerate(str_num)])


if __name__ == "__main__":
    s = Solution()
    print s.titleToNumber("Z")
