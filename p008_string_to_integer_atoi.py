#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @return an integer
    def atoi(self, str):
        from collections import deque

        first = True
        sign = 1
        numbers = deque()
        for c in str.lstrip():
            if first:
                first = False
                if c == '-':
                    sign = -1
                    continue
                elif c == '+':
                    continue

            if '0' <= c <= '9':
                numbers.appendleft(ord(c) - ord('0'))
            else:
                break

        ret = sum([e * 10 ** i for i, e in enumerate(numbers)]) * sign

        if ret > 2147483647:
            ret = 2147483647
        elif ret < -2147483648:
            ret = -2147483648

        return ret


if __name__ == '__main__':
    print(Solution().atoi('  -123abc'))
    print(Solution().atoi('2147483648'))
