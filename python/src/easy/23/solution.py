class ListNode:
    def __init__(self, val: int = 0, next: int | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:  # noqa: N802
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)

    def merge(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2

        return dummy.next

    # def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
    #     dummy = ListNode()
    #     curr = dummy
    #
    #     while True:
    #         min_node_idx = self.get_min_node_idx(lists)
    #         if min_node_idx is None:
    #             curr.next = None
    #             break
    #         curr.next = lists[min_node_idx]
    #         curr = curr.next
    #
    #     return dummy.next
    #
    # def get_min_node_idx(self, lists: list[ListNode | None]) -> int | None:
    #     min_node_idx, min_node_val = float("inf"), float("inf")
    #     for i, node in enumerate(lists):
    #         if node is None:
    #             continue
    #         if node.val < min_node_val:
    #             min_node_idx, min_node_val = i, node.val
    #     if min_node_val == float("inf"):
    #         return None
    #     return int(min_node_idx)
