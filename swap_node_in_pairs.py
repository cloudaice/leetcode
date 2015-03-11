#-*- coding: utf-8 -*-


from lib import *


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None:
            return head
        pre_head = ListNode(0)
        pre_head.next = head
        self.swap(pre_head)
        return pre_head.next

    def swap(self, node):
        if node.next is not None and node.next.next is not None:
            tmp1 = node.next
            tmp2 = node.next.next
            tmp3 = node.next.next.next
            node.next = tmp2
            tmp2.next = tmp1
            tmp1.next = tmp3
            self.swap(tmp1)

if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head = s.swapPairs(head)
    while head is not None:
        print head.val
        head = head.next
