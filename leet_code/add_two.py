from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val}, {self.next})'

    def __iter__(self):
        return self.next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Add two ll."""

        carry = 0
        l_first = ListNode(None, None)
        l_next = l_first
        iter_l1 = l1
        iter_l2 = l2

        while (iter_l1 is not None) or (iter_l2 is not None):
            val_1 = iter_l1.val if iter_l1 is not None else 0
            val_2 = iter_l2.val if iter_l2 is not None else 0

            sum_digit = val_1 + val_2 + carry
            carry, val = divmod(sum_digit, 10)

            res = ListNode(val, None)
            l_next.next = res

            l_next = res

            iter_l1 = iter_l1.next if iter_l1 is not None else None
            iter_l2 = iter_l2.next if iter_l2 is not None else None

        if carry > 0:
            l_next.next = ListNode(carry, None)

        return l_first.next


def to_list_nodes(arr):
    l_first = ListNode(None, None)
    l_next = l_first
    for val in arr:
        l_next.next = ListNode(val, None)
        l_next = l_next.next

    return l_first.next


def test_add_two():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    ll_1 = to_list_nodes(l1)
    ll_2 = to_list_nodes(l2)

    ll_3 = Solution().addTwoNumbers(ll_1, ll_2)

    l1 = [0]
    l2 = [0]

    l3_2 = Solution().addTwoNumbers(to_list_nodes(l1), to_list_nodes(l2))

    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]

    l3_3 = Solution().addTwoNumbers(to_list_nodes(l1), to_list_nodes(l2))