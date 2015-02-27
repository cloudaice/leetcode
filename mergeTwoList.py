#-*- coding: utf-8 -*-


from lib import *


class Solution:
    def mergeTwoLists(slef, l1, l2):
        pre_head = ListNode(0)
        current = pre_head

        node1 = l1
        node2 = l2
        while True:
            if node1 is None:
                current.next = node2
                break
            elif node2 is None:
                current.next = node1
                break
            else:
                if node1.val < node2.val:
                    current.next = node1
                    current = current.next
                    node1 = node1.next
                else:
                    current.next = node2
                    current = current.next
                    node2 = node2.next
        return pre_head.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l2 = ListNode(2)
    l2.next = ListNode(4)
    s = Solution()
    l = s.mergeTwoLists(l1, l2)
    while l is not None:
        print l.val
        l = l.next
