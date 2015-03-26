#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        ret = []
        for i in range(numRows):
            ret.append(Solution.getRow(i))
        return ret

    @staticmethod
    def getRow(rowIndex):
        ret = []
        for i in range(rowIndex + 1):
            ret.append(Solution.combine(rowIndex, i))
        return ret

    @staticmethod
    def combine(total, once):
        minus = total - once
        if minus > once:
            lagger = minus
            smaller = once
        else:
            lagger = once
            smaller = minus

        ret = 1
        for i in range(lagger + 1, total + 1):
            ret *= i
        for i in range(1, smaller + 1):
            ret //= i

        return ret


if __name__ == '__main__':
    print(Solution().generate(5))
