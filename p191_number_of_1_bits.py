#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        sum = 0
        while n:
            n &= n - 1  # this is used to delete the right "1" of n.
            sum += 1
        return sum

    def hammingWeight2(self, n):
        sum = 0
        while n:
            sum += n & 1
            n >>= 1
        return sum


if __name__ == '__main__':
    print(Solution().hammingWeight(11))
