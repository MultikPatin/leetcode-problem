class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:  # noqa: N802
        rev_head = None
        length = 0

        curr = head
        while curr:
            tmp = curr
            curr = curr.next
            rev_head = ListNode(tmp.val, rev_head)
            length += 1

        for _ in range(length // 2):
            if head.val != rev_head.val:
                return False
            head = head.next
            rev_head = rev_head.next

        return True
