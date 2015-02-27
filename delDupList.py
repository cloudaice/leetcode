#-*- coding: utf-8 -*-

from lib import *


class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head

        pre_node = head
        node = head.next
        pre_val = head.val
        while node is not None:
            if node.val == pre_val:
                pre_node.next = node.next
                node = node.next
            else:
                pre_node = node
                pre_val = node.val
                node = node.next
        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)

    s = Solution()
    node = s.deleteDuplicates(head)
    while node is not None:
        print node.val
        node = node.next
