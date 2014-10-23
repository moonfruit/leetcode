#!/usr/bin/python
# -*- utf-8 -*-

class Solution:
    def __init__(self, init='1'):
        self._list = [init]

    def countAndSay(self, n):
        while len(self._list) < n:
            self._list.append(self.say(self._list[-1]))
        return self._list[n-1]

    @staticmethod
    def say(string):
        ret = []
        save = None
        count = 1

        for c in string:
            if save is None:
                save = c

            elif c == save:
                count += 1

            else:
                ret.append('%d%s' % (count, save))
                save = c
                count = 1

        ret.append('%d%s' % (count, save))

        return ''.join(ret)


def main():
    solution = Solution()
    print(solution.countAndSay(10))
    print(solution._list)


if __name__ == '__main__':
    main()