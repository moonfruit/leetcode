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
    # @return a list of integers
    def preorderTraversal(self, root):
        ret = []
        if root is None:
            return ret
        else:
            ret.append(root.val)
            ret.extend(self.preorderTraversal(root.left))
            ret.extend(self.preorderTraversal(root.right))
        return ret


if __name__ == '__main__':
    from common import TreeNode
    root = TreeNode.new(1, 2, 3, None, None, None, 4, 5)
    root.print()
    print(Solution().preorderTraversal(root))
