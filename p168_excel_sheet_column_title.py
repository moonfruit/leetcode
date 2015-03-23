#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @return a string
    def convertToTitle(self, num):
       return Solution.cc(num)

    @staticmethod
    def c(n):
        return chr(ord('A') + n - 1)

    @staticmethod
    def cc(nn):
        from math import log
        l = int(log(nn, 26))
        r = nn
        nums = []

        for i in range(l, -1, -1):
            l = 26 ** i
            nums.append(r // l)
            r %= l

        while 0 in nums:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = 26
                    nums[i-1] -= 1

            if nums[0] == 0:
                nums.remove(0)

        return ''.join([Solution.c(e) for e in nums])


if __name__ == '__main__':
    s = Solution()
    print(s.convertToTitle(1))
    print(s.convertToTitle(26))
    print(s.convertToTitle(28))
    print(s.convertToTitle(52))
    print(s.convertToTitle(702))
