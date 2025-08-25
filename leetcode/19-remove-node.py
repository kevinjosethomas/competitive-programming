from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        cn = head

        history = []

        while cn.next is not None:
            history.append(cn)
            cn = cn.next

        history.append(cn)

        if len(history) < n + 1:
            head = head.next
        else:
            history[-n - 1].next = history[-n].next

        return head
