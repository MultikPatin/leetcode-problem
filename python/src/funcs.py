# Prefix Sum


def prefix_matrix(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    m = len(matrix[0])
    # Создаём матрицу из 0 с размером на 1 больше по вертикали и горизонтали
    ps = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    #  Заполняем префиксную матрицу
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Сумма всех элементов кроме текущего
            other = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]
            ps[i][j] = matrix[i - 1][j - 1] + other

    return ps


def prefix_array(nums: list[int]) -> list[int]:
    ps = [0]
    for n in nums:
        ps.append(ps[-1] + n)
    return ps


#  Linked List

type NextListNode = ListNode | None


class ListNode[T]:
    def __init__(self, val: T) -> None:
        self.val = val
        self.next: NextListNode = None


def reverse_linked_list(head: ListNode) -> NextListNode:
    prev = None
    curr = head
    while curr:
        tmp = curr
        curr = curr.next
        tmp.next = prev
        prev = tmp
    return prev


def middle_node(head: ListNode) -> NextListNode:
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def pre_middle_node(head: ListNode) -> NextListNode:
    fast = head
    slow = head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow
