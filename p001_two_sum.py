#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        map = {}
        for j, e in enumerate(num):
            jlist = map.get(e, [])
            jlist.append(j)
            map[e] = jlist

        for i, e in enumerate(num):
            remain = target - e
            jlist = map.get(remain)
            if jlist is not None:
                for j in jlist:
                    if i != j:
                        return i + 1, j + 1


    # 多次一举...
    def twoSum2(self, num, target):
        num1 = [e for e in enumerate(num) if e[1] % 2 == 0]
        num2 = [e for e in enumerate(num) if e[1] % 2 != 0]

        if target % 2 == 0:
            if len(num1) > len(num2):
                num1, num2 = num2, num1

            ret = Solution._sum1(num1, target)
            if ret:
                return ret
            return Solution._sum1(num2, target)

        else:
            return Solution._sum2(num1, num2, target)

    @staticmethod
    def _sum1(num, target):
        map = {}
        for j, e in num:
            jlist = map.get(e, [])
            jlist.append(j)
            map[e] = jlist

        for i, e in num:
            remain = target - e
            jlist = map.get(remain)
            if jlist is not None:
                for j in jlist:
                    if i != j:
                        return i + 1, j + 1

    @staticmethod
    def _sum2(num1, num2, target):
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        map2 = {}
        for j, e in num2:
            jlist = map2.get(e, [])
            jlist.append(j)
            map2[e] = jlist

        for i, e in num1:
            remain = target - e
            jlist = map2.get(remain)
            if jlist is not None:
                for j in jlist:
                    if i < j:
                        return i + 1, j + 1
                    elif i > j:
                        return j + 1, i + 1



if __name__ == '__main__':
    print(Solution().twoSum2([2, 7, 11, 14], 21))
    print(Solution().twoSum2([3, 2, 4], 6))

