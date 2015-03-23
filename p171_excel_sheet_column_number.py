#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        return Solution.nn(s)

    @staticmethod
    def nn(cc):
        i = len(cc)
        s = 0
        for e in cc:
            cur = Solution.n(e)
            i -= 1
            s += cur * 26 ** i
        return s

    @staticmethod
    def n(c):
        return ord(c.upper()) - ord('A') + 1


if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber('A'))
    print(s.titleToNumber('Z'))
    print(s.titleToNumber('AB'))
    print(s.titleToNumber('AZ'))
    print(s.titleToNumber('AYYYZ'))
