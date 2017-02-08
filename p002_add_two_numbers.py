# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        list = [str(self.val)]
        current = self.next
        while current is not None:
            list.append(str(current.val))
            current = current.next
        return '(' + ' -> '.join(list) + ')'


def toNumber(l):
    sum = i = 0
    while l is not None:
        sum += l.val * 10 ** i
        l = l.next
        i += 1
    return sum


def toList(n):
    current = head = ListNode(n % 10)
    while n >= 10:
        n //= 10
        node = ListNode(n % 10)
        current.next = node
        current = node
    return head


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return toList(toNumber(l1) + toNumber(l2))


class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = current = None
        s = 0
        c1 = l1
        c2 = l2
        while c1 is not None or c2 is not None:
            n1 = 0
            if c1 is not None:
                n1 = c1.val
                c1 = c1.next

            n2 = 0
            if c2 is not None:
                n2 = c2.val
                c2 = c2.next

            n = n1 + n2 + s
            s = n // 10
            n %= 10
            node = ListNode(n)
            if current is None:
                head = current = node
            else:
                current.next = node
                current = node

        if head is None:
            head = ListNode(s)

        elif s > 0:
            node = ListNode(s)
            current.next = node

        return head

if __name__ == '__main__':
    l = toList(10)
    print(l, toNumber(l))

    l1 = toList(123)
    print(l1, toNumber(l1))

    l2 = toList(567)
    print(l2, toNumber(l2))

    solution = Solution()
    ret = solution.addTwoNumbers(l1, l2)
    print(ret, toNumber(ret))

    solution = Solution2()
    ret = solution.addTwoNumbers(toList(1), toList(999))
    print(ret, toNumber(ret))
