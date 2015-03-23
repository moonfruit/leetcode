#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        cache = set()
        for a in A:
            if a in cache:
                cache.remove(a)
            else:
                cache.add(a)
        return cache.pop()


if __name__ == '__main__':
    print(Solution().singleNumber([2,2,1]))
    print(Solution().singleNumber([1,2,3,2,1]))
    print(Solution().singleNumber([1,2,3,4,5,6,7,8,9,9,8,7,6,5,3,2,1]))
