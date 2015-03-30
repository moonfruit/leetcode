#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        index = 5
        sum = 0
        while index <= n:
            sum += n // index
            index *= 5
        return sum

if __name__ == '__main__':
    print(Solution().trailingZeroes(5))
