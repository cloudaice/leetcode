#-*- coding: utf-8 -*-


class Solution:
    # @return a integer
    def convertToTitle(self, num):
        num_str = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        l = []
        a = num
        while a != 0:
            b = a % 26
            l.append(b)
            a = a / 26
        for i in range(len(l)):
            if l[i] <= 0:
                if i + 1 < len(l):
                    l[i + 1] = l[i + 1] - 1
                    l[i] = l[i] + 26
                else:
                    l.pop()

        l.reverse()
        result = ''.join([num_str[i - 1] for i in l])
        return result

if __name__ == "__main__":
    s = Solution()
    print s.convertToTitle(26)
