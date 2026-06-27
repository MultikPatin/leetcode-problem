package sort

// Временная сложность: O(n2)
// Пространственная сложность: O(1)
// Устойчивость: Устойчивая

func insertionSort(array []int) {
	for i := 1; i < len(array); i++ {
		itemToInsert := array[i]
		j := i
		for j > 0 && itemToInsert < array[j-1] {
			array[j] = array[j-1]
			j--
		}
		array[j] = itemToInsert
	}
}

//  ====================================== BY KEY

var digitLengths = [10]int{4, 4, 3, 3, 6, 4, 5, 4, 6, 6} // длины слов «ноль», «один»,...

func cardStrength(card int) int { // ключ сравнения
	return digitLengths[card]
}

func insertionSortByKey(array []int, key func(int) int) {
	for i := 1; i < len(array); i++ {
		itemToInsert := array[i]
		j := i
		// заменим сравнение itemToInsert < array[j-1] на сравнение ключей
		for j > 0 && key(itemToInsert) < key(array[j-1]) {
			array[j] = array[j-1]
			j--
		}
		array[j] = itemToInsert
	}
}

//  ====================================== BY COMPARATOR

var digitLengths1 = []int{4, 4, 3, 3, 6, 4, 5, 4, 6, 6} // длины слов «ноль», «один»,...

func isFirstCardWeaker(card1, card2 int) bool { // функция-компаратор
	return digitLengths1[card1] < digitLengths1[card2]
}

// воспользуемся уже знакомой сортировкой вставками
func insertionSortByComparator(array []int, less func(int, int) bool) {
	for i := 1; i < len(array); i++ {
		itemToInsert := array[i]
		j := i
		// заменим сравнение itemToInsert < array[j-1] на компаратор less
		for j > 0 && less(itemToInsert, array[j-1]) {
			array[j] = array[j-1]
			j--
		}
		array[j] = itemToInsert
	}
}
