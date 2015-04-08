#-*- coding: utf-8 -*-


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        rst, i = [], -1
        if numerator * denominator == 0:
            return "0"
        if numerator * denominator < 0:
            rst.append("-")
            i += 1
        a, b = abs(numerator), abs(denominator)
        rst.append(str(a / b))
        i += 1
        a = a % b
        if a != 0:
            rst.append(".")
            i += 1
        inx = {}
        while a != 0:
            a = a * 10
            rst.append(str(a / b))
            i += 1
            if a in inx:
                return "".join(rst[:inx[a]]) + "(" + "".join(rst[inx[a]: i]) + ")"
            inx[a] = i
            a = a % b
        return "".join(rst)

if __name__ == "__main__":
    s = Solution()
    print s.fractionToDecimal(1, 7)
    print s.fractionToDecimal(0, 7)
    print s.fractionToDecimal(-1, 7)
    print s.fractionToDecimal(8, 7)
    print s.fractionToDecimal(14, 7)
    print s.fractionToDecimal(10, 7)
    print s.fractionToDecimal(-7, 7)
    print s.fractionToDecimal(-4, 6)
    print s.fractionToDecimal(-1, 8)
