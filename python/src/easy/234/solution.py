class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:  # noqa: N802
        # 876
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 206
        prev = None
        curr = slow
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp

        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True
