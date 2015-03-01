#-*- coding: utf-8 -*-


class Solution:
    def hasCycle(self, head):
        if head is None:
            return False
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next
            if slow is fast:
                return True
        return False
