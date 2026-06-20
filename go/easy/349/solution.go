package main

func intersection(nums1 []int, nums2 []int) []int {
	set1 := make(map[int]bool)
	for _, num := range nums1 {
		set1[num] = true
	}

	set2 := make(map[int]bool)
	for _, num := range nums2 {
		set2[num] = true
	}

	result := make([]int, 0, len(set1))
	for num := range set1 {
		if set2[num] {
			result = append(result, num)
		}
	}

	return result
}
