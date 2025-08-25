from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = None
        output = None

        def l1():
            nonlocal head, output, list1
            if output is None:
                head = list1
                output = head
            else:
                output.next = list1
                output = output.next
            list1 = list1.next

        def l2():
            nonlocal head, output, list2
            if output is None:
                head = list2
                output = head
            else:
                output.next = list2
                output = output.next
            list2 = list2.next

        while list1 is not None or list2 is not None:

            if list1 is None:
                l2()
            elif list2 is None:
                l1()
            elif list1.val >= list2.val:
                l2()
            else:
                l1()

        return head
