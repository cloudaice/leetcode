#-*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head):
        if head is None:
            return
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        right = self.reverse(mid)

        left = head
        while True:
            if left is None:
                break
            next_left = left.next
            left.next = right
            left = next_left
            if right is None:
                break
            next_right = right.next
            right.next = left
            right = next_right

    def reverse(self, head):
        left = None
        right = head
        while head is not None:
            right = head.next
            head.next = left
            left = head
            head = right
        return left


if __name__ == "__main__":
    n = ListNode(1)
    head = n
    for i in range(2, 6):
        n.next = ListNode(i)
        n = n.next
    s = Solution()
    s.reorderList(head)

    while head is not None:
        print head.val
        head = head.next
