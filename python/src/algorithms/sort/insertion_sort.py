# Временная сложность: O(n2)
# Пространственная сложность: O(1)
# Устойчивость: Устойчивая


from collections.abc import Callable


def insertion_sort(array: list[int]) -> None:
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert


#  ====================================== BY KEY


digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...


def card_strength(card: int) -> int:  # ключ сравнения
    return digit_lengths[card]


# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_key(
    array: list[int], key_func: Callable[[int], int]
) -> None:
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на сравнение ключей
        while j > 0 and key_func(item_to_insert) < key_func(array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert


cards = [3, 7, 9, 2, 3]
insertion_sort_by_key(cards, card_strength)


#  ====================================== BY COMPARATOR


digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...


def is_first_card_weaker(
    card_1: int, card_2: int
) -> bool:  # функция-компаратор
    return digit_lengths[card_1] < digit_lengths[card_2]


# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_comparator(
    array: list[int], less: Callable[[int, int], bool]
) -> None:
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на компаратор less
        while j > 0 and less(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert


cards = [3, 7, 9, 2, 3]
insertion_sort_by_comparator(cards, is_first_card_weaker)
