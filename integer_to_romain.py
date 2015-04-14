#-*- coding: utf-8 -*-


class Solution:
    def intToRoman(self, num):
        qian = ["", "M", "MM", "MMM"]
        bai = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        shi = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ge = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        rst = ""
        rst += qian[num / 1000]
        num %= 1000
        rst += bai[num / 100]
        num %= 100
        rst += shi[num / 10]
        num %= 10
        rst += ge[num]
        return rst

if __name__ == "__main__":
    s = Solution()
    print s.intToRoman(29)
