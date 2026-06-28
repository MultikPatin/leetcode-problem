package sort

func mergeSort(array []int) []int {
	length := len(array)

	if length == 1 { // базовый случай рекурсии
		return array
	}

	mid := length // 2

	// запускаем сортировку рекурсивно на левой половине
	left := mergeSort(array[:mid])

	// запускаем сортировку рекурсивно на правой половине
	right := mergeSort(array[mid:])

	// заводим массив для результата сортировки
	result := make([]int, length)

	// сливаем результаты
	l, r, k := 0, 0, 0
	for l < len(left) && r < len(right) {
		// выбираем, из какого массива забрать минимальный элемент
		if left[l] <= right[r] {
			result[k] = left[l]
			l++
		} else {
			result[k] = right[r]
			r++
		}
		k++
	}

	// Если один массив закончился раньше, чем второй, то
	// переносим оставшиеся элементы второго массива в результирующий
	for l < len(left) {
		result[k] = left[l] // перенеси оставшиеся элементы left в result
		l++
		k++
	}
	for r < len(right) {
		result[k] = right[r] // перенеси оставшиеся элементы right в result
		r++
		k++
	}

	return result
}
