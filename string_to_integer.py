#-*- coding: utf-8 -*-


class Solution:
    def atoi(self, str):
        s = str.strip()
        negative = False
        if len(s) > 0:
            if s[0] == "-":
                negative = True
                s = s[1:]
            elif s[0] == "+":
                s = s[1:]

        digit = ""
        for i in s:
            if i.isdigit():
                digit += i
            else:
                break
        rst = 0
        if digit == "":
            return rst

        if negative:
            rst = 0 - int(digit)
        else:
            rst = int(digit)

        if rst > 2147483647:
            return 2147483647
                             
        if rst < -2147483648:
            return -2147483648
        return rst

if __name__ == "__main__":
    s = Solution()
    print s.atoi("  -0012a42")
    print s.atoi("-+1")
