from python.src.helper import Fields, tester


class ListNode:
    def __init__(self, val: int = 0, next: int | None = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        res = f"{self.val} "

        if self.next:
            res += str(self.next)

        return res


def init_node(num: list[int]) -> ListNode | None:
    if not num:
        return None

    head = ListNode(num[0])
    tmp = head

    for n in num[1:]:
        node = ListNode(n)
        tmp.next = node
        tmp = node

    return head


test_data = [
    {
        Fields.args: (init_node([1, 2, 4]), init_node([1, 3, 4])),
        Fields.expd: init_node([1, 1, 2, 3, 4, 4]),
    },
    {Fields.args: (init_node([1]), init_node([])), Fields.expd: init_node([1])},
    {Fields.args: (init_node([]), init_node([])), Fields.expd: init_node([])},
    {Fields.args: (init_node([]), init_node([0])), Fields.expd: init_node([0])},
]


class Solution:
    # def mergeTwoLists(  # noqa: N802
    #     self, list1: ListNode | None, list2: ListNode | None
    # ) -> ListNode | None:
    #     if list1 is None and list2 is None:
    #         return None
    #
    #     if list1 is None:
    #         node = ListNode(list2.val)
    #         node.next = self.mergeTwoLists(list1, list2.next)
    #     elif list2 is None:
    #         node = ListNode(list1.val)
    #         node.next = self.mergeTwoLists(list1.next, list2)
    #     elif list1.val > list2.val:
    #         node = ListNode(list2.val)
    #         node.next = self.mergeTwoLists(list1, list2.next)
    #     else:
    #         node = ListNode(list1.val)
    #         node.next = self.mergeTwoLists(list1.next, list2)
    #
    #     return node

    def mergeTwoLists(  # noqa: N802
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    tester(func=solution.mergeTwoLists, test_data=test_data)
