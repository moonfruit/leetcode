#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        copy = [e for e in nums]
        l = len(nums)
        k = l - k % l
        for i in range(l):
            nums[i] = copy[(k + i) % l]


    def rotate2(self, nums, k):
        if not nums:
            return

        l = len(nums)
        for i in range(k % l):
            last = nums[-1]
            for j in range(l-1, 0, -1):
                nums[j] = nums[j-1]
            nums[0] = last

    def rotate3(self, nums, k):
        # Todo third method
        # Fixme rotate([1, 2, 3, 4, 5, 6], 2)
        if not nums:
            return
        l = len(nums)
        k = k % l
        if k == 0:
            return

        last = nums[0]
        cur = k
        for e in nums:
            nums[cur], last = last, nums[cur]
            cur = (cur + k) % l


if __name__ == '__main__':
    s = Solution()
    l = [1, 2, 3, 4, 5, 6, 7]
    print(l)
    l = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(l, 0)
    print(l)
    l = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(l, 3)
    print(l)
    l = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(l, 6)
    print(l)
    l = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(l, 9)
    print(l)

    l = [1, 2, 3, 4, 5, 6]
    s.rotate(l, 2)
    print(l)
