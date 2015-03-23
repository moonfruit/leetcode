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
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        ret = []
        if not root:
            return ret

        ret.append([root.val])

        parents = [root]
        childs = []

        while True:
            for e in parents:
                if e.left:
                    childs.append(e.left)
                if e.right:
                    childs.append(e.right)

            if childs:
                ret.append([e.val for e in childs])
                parents = childs
                childs = []

            else:
                break

        ret.reverse()
        return ret


if __name__ == '__main__':
    from common import TreeNode
    print(Solution().levelOrderBottom(TreeNode.new(3, 9, 20, None, None, 15, 7)))
