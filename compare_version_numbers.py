#-*- coding: utf-8 -*-


class Solution:
    def compareVersion(self, version1, version2):
        s1 = version1.split(".")
        s2 = version2.split(".")
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            for i in range(l1 - l2):
                s2.append("0")
        if l2 > l1:
            for i in range(l2 - l1):
                s1.append("0")

        merge = zip([int(item) for item in s1], [int(item) for item in s2])
        for item in merge:
            if item[0] > item[1]:
                return 1
            if item[0] < item[1]:
                return -1
        return 0


if __name__ == "__main__":
    s = Solution()
    print s.compareVersion("2.1", "10.23.33")
