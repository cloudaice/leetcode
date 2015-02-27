#-*- coding: utf-8 -*-

# 相对于1稍微复杂一些，需要处理多个连续相同的情况

from lib import *


class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head

        pre_head = ListNode(0)
        pre_head.next = head
        pre_pre_node = pre_head
        pre_node = head
        node = head.next
        while node is not None:
            if node.val == pre_node.val:
                node = node.next
                while node is not None:
                    if node.val != pre_node.val:
                        break
                    node = node.next
                pre_node = node
                pre_pre_node.next = pre_node
                if pre_node is None:
                    break
                node = pre_node.next
            else:
                pre_node = node
                pre_pre_node = pre_pre_node.next
                node = node.next

        return pre_head.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    #head.next.next.next = ListNode(3)
    #head.next.next.next.next = ListNode(4)
    #head.next.next.next.next.next = ListNode(4)
    #head.next.next.next.next.next.next = ListNode(5)

    s = Solution()
    node = s.deleteDuplicates(head)
    while node is not None:
        print node.val
        node = node.next
