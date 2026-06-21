from src.helper import Fields, tester


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:  # noqa: N802
        length = 0

        curr = head
        while curr.next is not None:
            curr = curr.next
            length += 1

        del_idx = length // 2 if length % 2 == 0 else length // 2 + 1

        curr = head
        for i in range(del_idx):
            curr = curr.next

        return curr
