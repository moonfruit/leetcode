#!/usr/bin/python
# -*- utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        print("----")
        cur = self
        while cur:
            print("%d - %d" % (id(cur), cur.val))
            cur = cur.next

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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

    @staticmethod
    def new(*args):
        if not args or args[0] is None:
            return None

        root = None
        parents = []
        childs = []
        for e in args:
            if not root:
                root = TreeNode(e)
                parents.append(root)
                continue

            if e is not None:
                e = TreeNode(e)

            childs.append(e)

            if len(childs) >= len(parents) * 2:
                for p, (x, y) in zip(parents, zip(*[iter(childs)]*2)):
                    p.left = x
                    p.right = y

                parents = [e for e in childs if e is not None]
                childs = []

        if len(childs) > 0:
            if len(childs) % 2 == 1:
                childs.append(None)
            for p, (x, y) in zip(parents, zip(*[iter(childs)]*2)):
                p.left = x
                p.right = y

        return root
