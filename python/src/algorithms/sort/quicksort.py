import random


def partition(
    array: list[int], pivot: int
) -> tuple[list[int], list[int], list[int]]:
    left = [x for x in array if x < pivot]
    center = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return left, center, right


def quicksort(array: list[int]) -> list[int]:
    if len(array) < 2:
        return array  # массивы с 0 или 1 элементами фактически отсортированы
    pivot = random.choice(array)  # noqa: S311
    left, center, right = partition(array, pivot)
    return quicksort(left) + center + quicksort(right)
