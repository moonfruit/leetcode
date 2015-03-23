#!/usr/bin/python
# -*- utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head:
            return head

        cur = head
        l = 1
        while cur.next:
            l += 1
            cur = cur.next
        cur.next = head

        for i in range((l - k % l) % l):
            cur = cur.next
        head = cur.next
        cur.next = None

        return head


if __name__ == '__main__':
    from leetcode import ListNode
    list = ListNode.new(1, 2, 3, 4, 5)
    list.print()
    Solution().rotateRight(list, 0).print()
