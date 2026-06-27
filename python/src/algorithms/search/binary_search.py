# Временная сложность: O(log n)
# Отсортированный массив делится пополам на каждой итерации


def binary_search(arr: list[int], x: int, left: int, right: int) -> int:
    if right <= left:  # промежуток пуст
        return -1
    # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x:  # центральный элемент — искомый
        return mid
    if x < arr[mid]:
        # искомый элемент меньше центрального значит следует искать в левой половине
        return binary_search(arr, x, left, mid)
    # иначе следует искать в правой половине
    return binary_search(arr, x, mid + 1, right)
