#!/usr/bin/python
# -*- utf-8 -*-

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return None

        from copy import copy

        old = head
        new = ret = copy(head)
        save = {None: None, old: new}
        while old.next:
            old = old.next
            save[old] = new.next = copy(old)
            new = new.next

        new = ret
        while new:
            new.random = save[new.random]
            new = new.next

        return ret


if __name__ == '__main__':
    from leetcode import RandomListNode
    head = RandomListNode.new(1,2,3,4,5,6)
    head.print()
    Solution().copyRandomList(head).print()
