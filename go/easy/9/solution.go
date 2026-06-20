package main

// func isPalindrome(x int) bool {
// 	if x < 0 {
// 		return false
// 	}
// 	numbers := []int{}
// 	for x > 0 {
// 		numbers = append(numbers, x%10)
// 		x /= 10
// 	}
// 	r := 0
// 	l := len(numbers) - 1
// 	for l > r {
// 		if numbers[r] == numbers[l] {
// 			r += 1
// 			l -= 1
// 		} else {
// 			return false
// 		}
// 	}
// 	return true
// }

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	origin := x
	rev := 0
	for x > 0 {
		rev = rev*10 + x%10
		x /= 10
	}
	return rev == origin
}

//12345
// 0*10 + 5 = 5 // 1234
// 5*10 + 4 = 54 // 123
// 54*10 + 3 = 543 // 12
// 543*10 + 2 = 5432 // 1
// 5432*10 + 1 = 54321 // 0
