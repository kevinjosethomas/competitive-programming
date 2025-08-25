# O(N*K)
"""
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
"""

# Received hint: Think about replacing your minimize scan with a structure that always lets you pull the smallest current node in O(log k) time rather than O(k). What data structure gives you that?

import heapq
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

        queue = [
            (x.val if x is not None else 0, i, x) for i, x in enumerate(lists)
        ]
        heapq.heapify(queue)
        head = None
        tail = None

        while len(queue):
            _, i, node = heapq.heappop(queue)

            if node is None:
                continue

            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = tail.next

            if node.next is not None:
                heapq.heappush(queue, (node.next.val, i, node.next))

        return head
