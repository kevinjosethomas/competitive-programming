from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def minimize(l: List[Optional[ListNode]]):
    smallest = None
    index = -1
    for i, v in enumerate(l):
        if v is None:
            continue
        if smallest is None:
            smallest = v
            index = i
        if v.val < smallest.val:
            smallest = v
            index = i

    return smallest, index


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        head = None
        tail = None

        while any(lists):
            smallest, index = minimize(lists)

            if head is None:
                head = smallest
                tail = smallest
            else:
                tail.next = smallest
                tail = tail.next
            lists[index] = lists[index].next

        return head
