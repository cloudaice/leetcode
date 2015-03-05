#-*- coding: utf-8 -*-


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        m = prices[0]
        i = 1
        s = 0
        while i < len(prices):
            if prices[i] < prices[i - 1]:
                s = s + prices[i - 1] - m
                m = prices[i]
            i += 1
        s = s + prices[i - 1] - m
        return s


if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([1, 3, 5, 2, 7])
