#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    # @return an integer
    def atoi(self, str):
        first = True
        sign = 1
        sum = 0
        overflow = 0
        for c in str.lstrip():
            if first:
                first = False
                if c == '-':
                    sign = -1
                    continue
                elif c == '+':
                    continue

            if '0' <= c <= '9':
                cur = ord(c) - ord('0')
                if overflow > 1:
                    return 2147483647 if sign == 1 else -2147483648

                elif overflow > 0:
                    if cur < 8:
                        overflow = 2
                    elif cur == 8:
                        if sign == 1:
                            return 2147483647
                        else:
                            overflow = 2
                    else:
                        return 2147483647 if sign == 1 else -2147483648

                sum = sum * 10 + cur
                if sum > 214748364:
                    overflow = 2
                elif sum == 214748364:
                    overflow = 1
            else:
                break

        return sum * sign


if __name__ == '__main__':
    print(Solution().atoi(''))
    print(Solution().atoi('  -123abc'))
    print(Solution().atoi('2147483648'))
