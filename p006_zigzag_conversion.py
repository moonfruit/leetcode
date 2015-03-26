#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if not s:
            return s

        if nRows == 1:
            return s

        matrix = []
        length = len(s)
        for start in range(0, length, nRows * 2 - 2):
            for i in range(nRows * 2 - 2):
                if i == 0:
                    matrix.append([s[start]] + [''] * (nRows - 1))

                elif i < nRows:
                    if start + i < length:
                        matrix[-1][i] = s[start + i]

                else:
                    if start + i < length:
                        matrix.append([''] * (nRows * 2 - 2 - i) + [s[start + i]] + [''] * (i - nRows + 1))

        ret = ''
        for i in range(nRows):
            ret += ''.join([x[i] for x in matrix])

        return ret


if __name__ == '__main__':
    print(Solution().convert('ABC', 2))
    print(Solution().convert('PAYPALISHIRING', 3))
    print(Solution().convert('PAYPALISHIRING', 4))

