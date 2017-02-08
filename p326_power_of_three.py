#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        from math import log
        l = round(log(n, 3))
        return n == 3 ** l


if __name__ == '__main__':
    print(Solution().isPowerOfThree(28))
    print(Solution().isPowerOfThree(27))
    print(Solution().isPowerOfThree(81))
    print(Solution().isPowerOfThree(243))
