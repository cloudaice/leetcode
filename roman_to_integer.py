# -*- coding: utf-8 -*-


class Solution:
    def romanToInt(self, s):
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ss = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and m[s[i + 1]] > m[s[i]]:
                ss += m[s[i + 1]] - m[s[i]]
                i += 2
            else:
                ss += m[s[i]]
                i += 1
        return ss

if __name__ == "__main__":
    s = Solution()
    print s.romanToInt("MMMCMXCIX")
