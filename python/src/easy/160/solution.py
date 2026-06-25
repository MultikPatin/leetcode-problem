# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(  # noqa: N802
        self,
        headA: ListNode,
        headB: ListNode,  # noqa: N803
    ) -> ListNode | None:
        node_set = set()
        node_a = headA
        node_b = headB

        while node_a or node_b:
            if node_a:
                if node_a in node_set:
                    return node_a
                node_set.add(node_a)
                node_a = node_a.next
            if node_b:
                if node_b in node_set:
                    return node_b
                node_set.add(node_b)
                node_b = node_b.next
        return None

    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     pA = headA  # стартуем с головы A
    #     pB = headB  # стартуем с головы B
    #
    #     while pA != pB:  # пока не встретились (включая случай None)
    #         # Если pA не NULL — идём дальше по A, иначе — переключаемся на B
    #         pA = pA.next if pA else headB
    #
    #         # Аналогично для pB: если дошёл до конца B — идём в A
    #         pB = pB.next if pB else headA
    #
    #     # вышли, когда pA == pB:
    #     #   - если они оба указывают на узел — это и есть пересечение
    #     #   - если оба None — пересечения нет
    #     return pA
