package main

func reverseString(s []byte) {
	le := 0
	rt := len(s) - 1

	for le < rt {
		temp := s[le]
		s[le] = s[rt]
		s[rt] = temp
		le += 1
		rt -= 1
	}
}
