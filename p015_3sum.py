#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        ret = []

        length = len(num)
        if length < 3:
            return ret

        num.sort()
        for a in range(length - 2):
            if a == 0 or num[a] > num[a-1]:
                b = a + 1
                c = length - 1
                while b < c:
                    sum = num[a] + num[b] + num[c]
                    if sum == 0:
                        ret.append([num[a], num[b], num[c]])

                        b += 1
                        while b < c and num[b] == num[b-1]:
                            b += 1

                        c -= 1
                        while b < c and num[c] == num[c+1]:
                            c -= 1

                    elif sum < 0:
                        b += 1
                        while b < c and num[b] == num[b-1]:
                            b += 1

                    else:
                        c -= 1
                        while b < c and num[c] == num[c+1]:
                            c -= 1

        return ret

    def threeSum2(self, num):
        l = len(num)
        two = {}
        for i in range(l):
            for j in range(i + 1, l):
                a, b = num[i], num[j]
                sum = a + b
                list = two.get(sum)
                if list is None:
                    two[sum] = [((a, i), (b, j))]
                else:
                    list.append(((a, i), (b, j)))

        ret = set()
        for k, c in enumerate(num):
            list = two.get(-c)
            if list is None:
                continue
            for (a, i), (b, j) in list:
                if k not in (i, j):
                    ret.add(tuple(sorted([a, b, c])))

        return [[a, b, c] for (a, b, c) in ret]


if __name__ == '__main__':
    def printit(list):
        print('----')
        print(len(list))
        print(sorted(list))

    printit(Solution().threeSum([-1, 0, 1, 2 ,-1, -4]))
    printit(Solution().threeSum2([-1, 0, 1, 2 ,-1, -4]))

    printit(Solution().threeSum([-12,4,12,-4,3,2,-3,14,-14,3,-12,-7,2,14,-11,3,-6,6,4,-2,-7,8,8,10,1,3,10,-9,8,5,11,3,-6,0,6,12,-13,-11,12,10,-1,-15,-12,-14,6,-15,-3,-14,6,8,-9,6,1,7,1,10,-5,-4,-14,-12,-14,4,-2,-5,-11,-10,-7,14,-6,12,1,8,4,5,1,-13,-3,5,10,10,-1,-13,1,-15,9,-13,2,11,-2,3,6,-9,14,-11,1,11,-6,1,10,3,-10,-4,-12,9,8,-3,12,12,-13,7,7,1,1,-7,-6,-13,-13,11,13,-8]))
    printit(Solution().threeSum2([-12,4,12,-4,3,2,-3,14,-14,3,-12,-7,2,14,-11,3,-6,6,4,-2,-7,8,8,10,1,3,10,-9,8,5,11,3,-6,0,6,12,-13,-11,12,10,-1,-15,-12,-14,6,-15,-3,-14,6,8,-9,6,1,7,1,10,-5,-4,-14,-12,-14,4,-2,-5,-11,-10,-7,14,-6,12,1,8,4,5,1,-13,-3,5,10,10,-1,-13,1,-15,9,-13,2,11,-2,3,6,-9,14,-11,1,11,-6,1,10,3,-10,-4,-12,9,8,-3,12,12,-13,7,7,1,1,-7,-6,-13,-13,11,13,-8]))
