#-*- coding: utf-8 -*-


# 常数时间返回栈里面的最小值, 这个可以根据栈的特性，每次往栈压数据的时候，检查新加的数据是否小于等于已有栈的最小数据。
# 如果是的话，则将该数据放入一个队列。每次出栈的时候，检查出去的是否是当前最小值，是的话，从队列中把相应的最后一个值出栈。
# 反证法可以证明该方法的正确性


class MinStack:
    def __init__(self):
        self.stack = []
        self.minS = []

    def push(self, x):
        self.stack.append(x)
        if self.minS == []:
            self.minS.append(x)
        else:
            if x <= self.minS[-1]:
                self.minS.append(x)
        return x

    def pop(self):
        n = self.stack.pop()
        if self.minS[-1] == n:
            self.minS.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minS[-1]

if __name__ == "__main__":
    s = MinStack()
    print s.push(1)
    print s.push(8)
    print s.push(6)
    s.pop()
    print s.top()
    print s.getMin()
