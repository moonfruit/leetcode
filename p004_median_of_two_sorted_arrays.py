#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        la = len(A)
        lb = len(B)
        total = la + lb
        half = total // 2 + total % 2
        i = j = m = 0
        while i + j < half:
            if i >= la:
                m = B[j]
                j += 1
            elif j >= lb:
                m = A[i]
                i += 1
            else:
                if A[i] < B[j]:
                    m = A[i]
                    i += 1
                else:
                    m = B[j]
                    j += 1

        if total % 2 == 0:
            if i >= la:
                m2 = B[j]
            elif j >= lb:
                m2 = A[i]
            else:
                if A[i] < B[j]:
                    m2 = A[i]
                else:
                    m2 = B[j]
            m = (m + m2) / 2.0

        return float(m)

    def findMedianSortedArrays2(self, A, B):
        mix = sorted(A + B)
        length = len(mix)
        if length % 2 == 0:
            return (mix[length // 2 - 1] + mix[length // 2]) / 2.0
        else:
            return float(mix[length // 2])


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays2([], [1]))
    print(Solution().findMedianSortedArrays2([1, 4, 6, 7], [2, 3, 5]))
    print(Solution().findMedianSortedArrays2([1, 4, 6, 7], [2, 3, 5, 8]))
