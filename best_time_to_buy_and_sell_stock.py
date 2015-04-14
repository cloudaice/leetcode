#-*- coding: utf-8 -*-


class Solution:
    def maxProfit(self, prices):
        val = 0
        if len(prices) == 0:
            return val

        Min, Max = prices[0], prices[0]
        
        for p in prices:
            if p < Min:
                val = max(val, Max - Min)
                Min, Max = p, p
            if p > Max:
                Max = p
        return max(val, Max - Min)

if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([2, 5, 1, 3])
