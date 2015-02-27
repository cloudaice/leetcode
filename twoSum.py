#-*- coding: utf-8 -*-


class Solution:
    def twoSum(slef, num, target):
        m = {}
        for i in range(len(num)):
            if num[i] in m:
                m[num[i]].append(i + 1)
            else:
                m[num[i]] = [i + 1]
        for item in num:
            if target - item in m:
                if target - item == item:
                    if len(m[item]) >= 2:
                        return (m[item][0], m[item][1])
                else:
                    return (m[item][0], m[target - item][0])
                    

if __name__ == "__main__":
    s = Solution()
    print s.twoSum([3, 2, 4], 6)
