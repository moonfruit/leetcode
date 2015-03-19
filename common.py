#!/usr/bin/python
# -*- utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def new(*args):
        head = None
        last = None
        for e in args:
            node = ListNode(e)
            if head is None:
                head = node
            if last is not None:
                last.next = node
            last = node

        return head

    def print(self):
        print("----")
        cur = self
        while cur:
            print("%d - %d" % (id(cur), cur.val))
            cur = cur.next


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def new(*args):
        return TreeNode._new(*args)[0]

    @staticmethod
    def _new(*args):
        if not args:
            return None, args
        root, args = TreeNode(args[0]), args[1:]
        if root.val is None:
            return None, args
        root.left, args = TreeNode._new(*args)
        root.right, args = TreeNode._new(*args)
        return root, args

    def _print(self):
        print("%d - %d" % (id(self), self.val))
        if self.left:
            self.left._print()
        else:
            print(id(None), None)
        if self.right:
            self.right._print()
        else:
            print(id(None), None)

    def print(self):
        print("----")
        self._print()
