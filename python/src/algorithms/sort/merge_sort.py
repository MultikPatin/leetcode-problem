def merge_sort(array: list[int]) -> list[int]:
    length = len(array)

    if length == 1:  # базовый случай рекурсии
        return array

    mid = length // 2

    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[:mid])

    # запускаем сортировку рекурсивно на правой половине
    right = merge_sort(array[mid:])

    # заводим массив для результата сортировки
    result = [0] * length

    # сливаем результаты
    lf, rt, k = 0, 0, 0
    while lf < len(left) and rt < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[lf] <= right[rt]:
            result[k] = left[lf]
            lf += 1
        else:
            result[k] = right[rt]
            rt += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while lf < len(left):
        result[k] = left[lf]  # перенеси оставшиеся элементы left в result
        lf += 1
        k += 1
    while rt < len(right):
        result[k] = right[rt]  # перенеси оставшиеся элементы right в result
        rt += 1
        k += 1

    return result


if __name__ == "__main__":
    array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_array = merge_sort(array)
    print(sorted_array)
