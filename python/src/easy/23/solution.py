class ListNode:
    def __init__(self, val: int = 0, next: int | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    # def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
    #     min_node_idx = self.get_min_node_idx(lists)
    #     if min_node_idx is None:
    #         return None
    #     curr = head = lists[min_node_idx]
    #     lists[min_node_idx] = lists[min_node_idx].next
    #
    #     while True:
    #         min_node_idx = self.get_min_node_idx(lists)
    #         if min_node_idx is None:
    #             curr.next = None
    #             break
    #         curr.next = lists[min_node_idx]
    #         curr = curr.next
    #
    #     return head

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        dummy = ListNode()
        curr = dummy

        while True:
            min_node_idx = self.get_min_node_idx(lists)
            if min_node_idx is None:
                curr.next = None
                break
            curr.next = lists[min_node_idx]
            curr = curr.next

        return dummy.next

    def get_min_node_idx(self, lists: list[ListNode | None]) -> int | None:
        min_node_idx, min_node_val = float("inf"), float("inf")
        for i, node in enumerate(lists):
            if node is None:
                continue
            if node.val < min_node_val:
                min_node_idx, min_node_val = i, node.val
        if min_node_val == float("inf"):
            return None
        return int(min_node_idx)
