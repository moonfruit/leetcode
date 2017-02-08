#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        from re import match
        return not not match(r'^\s*[+-]?((\d+\.?\d*)|(\.\d+))(e[+-]?\d+)?\s*$', s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.isNumber(""))
    print(solution.isNumber(" "))
    print(solution.isNumber("123.1"))
    print(solution.isNumber("123.1"))
    print(solution.isNumber(".1"))
    print(solution.isNumber("1"))
    print(solution.isNumber("e10"))
