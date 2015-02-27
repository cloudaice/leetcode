#-*- coding: utf-8 -*-

# 正向计算链表长度，然后减去倒数的个数，然后再次遍历计数，移除即可，注意边界情况


from lib import *


class Solution:
    def removeNthFromEnd(self, head, n):
        if head is None:
            return head
        count = 0
        node = head
        while node is not None:
            node = node.next
            count += 1
        count = count - n
        # 移除头节点
        if count == 0:
            return head.next

        cnt = 0
        node = head
        while node is not None:
            cnt += 1
            if cnt == count:
                if node.next is None:
                    return head
                node.next = node.next.next
                break
            node = node.next
        return head

if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    node = ListNode(2)
    head.next = node
    for i in range(3, 6):
        node.next = ListNode(i)
        node = node.next
    node = s.removeNthFromEnd(head, 5)
    while node is not None:
        print node.val
        node = node.next
