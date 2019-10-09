"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        l = ListNode(0)
        l_copy = l
        carry = 0
        while l1 or l2:
            l1_val = l1.val if (l1 and l1.val) else 0
            l2_val = l2.val if (l2 and l2.val) else 0
            two_sum = l1_val + l2_val + carry
            if two_sum >= 10:
                l_copy.next = ListNode(two_sum % 10)
                carry = 1
            else:
                l_copy.next = ListNode(two_sum)
                carry = 0
            l_copy = l_copy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry == 1:
            l_copy.next = ListNode(1)
        return l.next
