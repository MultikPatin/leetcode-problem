def insertion_sort(array: list[int]) -> None:
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
