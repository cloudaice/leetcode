#-*- coding: utf-8 -*-


class Solution:
    def countAndSay(self, n):

        def generate(seq):
            nextSeq = ""
            l = len(seq)
            b = seq[0]
            count = 1
            i = 1
            while i < l:
                if seq[i] == b:
                    count += 1
                else:
                    nextSeq += str(count) + b
                    b = seq[i]
                    count = 1
                i += 1
            nextSeq += str(count) + b
            return nextSeq

        result = "1"
        for i in range(n - 1):
            result = generate(result)
        return result

if __name__ == "__main__":
    s = Solution()
    print s.countAndSay(5)
