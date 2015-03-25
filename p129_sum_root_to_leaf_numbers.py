#!/usr/bin/python
# -*- utf-8 -*-

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0

        self._travel(root)

        total = []
        for t in self.routes:
            for i, e in enumerate(t):
                try:
                    total[i] += e
                except:
                    total.append(e)

        return sum([e * 10 ** i for i, e in enumerate(total)])

    def __init__(self):
        from collections import deque
        self.route = deque()
        self.routes = []

    def _travel(self, node):
        self.route.appendleft(node.val)

        if node.left is None and node.right is None:
            self.routes.append(tuple(self.route))

        else:
            if node.left is not None:
                self._travel(node.left)

            if node.right is not None:
                self._travel(node.right)

        self.route.popleft()


if __name__ == '__main__':
    from leetcode import TreeNode
    root = TreeNode.new(1,2,3,4,5,6,7,8,9,0)
    print(Solution().sumNumbers(root))
