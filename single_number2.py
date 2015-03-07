#-*- coding: utf-8 -*-


# 这道题目比较恶心，最简单的方法就是使用hash表，也就是Python的字典保存每个数字出现的次数，然后输出只是出现一个的那个数字。
# 最优的解法是从位的角度考虑，计算每一位'1'出现的次数，因为其它数字都会出现三次，因此总次数对3取余得到的就是要找的那个数对应位上的数。

class Solution:
    def singleNumber(self, A):
        m = {}
        for a in A:
            if a not in m:
                m[a] = 1
            else:
                m[a] = m[a] + 1
        for k, v in m.items():
            if v == 1:
                return k

    def singleNumber2(self, A):
        bit1 = 0
        bit2 = 0
        for i in A:
            oldbit1 = bit1
            bit1 = bit1 ^ (i & (~bit2))
            bit2 = (oldbit1 & i) | (bit2 & (~i))
        return bit1

if __name__ == "__main__":
    s = Solution()
    print s.singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2])
