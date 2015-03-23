#!/usr/bin/python
# -*- utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        last = None
        curr = head
        next = curr and curr.next or None

        while curr is not None and next is not None:
            if last is None:
                head = next
            else:
                last.next = next

            curr.next = next.next
            next.next = curr

            last = curr
            curr = curr.next
            next = curr and curr.next or None

        return head


if __name__ == '__main__':
    from leetcode import ListNode
    list = ListNode.new(1, 2, 3, 4, 5)
    list.print()
    Solution().swapPairs(list).print()
