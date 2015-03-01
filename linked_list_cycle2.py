#-*- coding: utf-8 -*-


class Solution:
    def detectCycle(self, head):
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                find = head
                while find is not slow:
                    slow = slow.next
                    find = find.next
                return find
        return None
