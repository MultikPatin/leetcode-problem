class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:  # noqa: N802
        tmp = self.pre_middle_node(head)
        p2 = self.reverse_list(tmp.next)

        tmp.next = None

        new = p1 = head
        while p2:
            p1_next = p1.next
            p1.next = p2
            p1 = p2
            p2 = p1_next
        return new

    def reverse_list(self, head: ListNode | None) -> ListNode | None:  # noqa: N802
        prev = None
        curr = head
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
        return prev

    def pre_middle_node(self, head: ListNode | None) -> ListNode | None:
        fast = head
        slow = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow
