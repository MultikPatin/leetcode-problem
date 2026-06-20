package main

func twoSum(nums []int, target int) []int {
	cache := make(map[int]int)

	for n := range nums {
		res := target - nums[n]
		if _, ok := cache[res]; ok {
			return []int{cache[res], n}
		}
		cache[nums[n]] = n
	}

	return nil
}
