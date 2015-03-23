#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        cache = {}
        for a in A:
            count = cache.get(a, 0) + 1
            if count >= 3:
                cache.pop(a)
            else:
                cache[a] = count
        return cache.popitem()[0]


if __name__ == '__main__':
    print(Solution().singleNumber([1,2,3,2,1,2,3,1]))