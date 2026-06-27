package sort

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
