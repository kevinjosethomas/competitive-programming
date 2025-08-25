# from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def removeNthFromEnd(
#         self, head: Optional[ListNode], n: int
#     ) -> Optional[ListNode]:
#         cn = head

#         history = []

#         while cn.next is not None:
#             history.append(cn)
#             cn = cn.next

#         history.append(cn)

#         if len(history) < n + 1:
#             head = head.next
#         else:
#             history[-n - 1].next = history[-n].next

#         return head


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        first = head
        second = head

        for _ in range(n):
            second = second.next

        if second is None:
            return head.next

        while True:
            if second.next is None:
                first.next = first.next.next
                break

            first = first.next
            second = second.next

        return head
