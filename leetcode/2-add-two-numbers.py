from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def condense(num: str, node: ListNode) -> str:
            new_num = str(node.val) + num
            return (
                new_num if node.next is None else condense(new_num, node.next)
            )

        def split(num: str) -> ListNode:
            original = ListNode()
            current = original

            for char in reversed(num):
                current.next = ListNode(int(char))
                current = current.next

            return original.next

        added = int(condense("", l1)) + int(condense("", l2))

        return split(str(added))
