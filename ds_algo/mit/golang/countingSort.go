package main

import (
	"fmt"
)

var arr = []int{91, 28, 73, 46, 55, 64, 37, 82, 19}

func main() {
	fmt.Println("before", arr)
	countingSort(arr)
	fmt.Println("after:", arr)
}

func countingSort(list []int) {
	var min, max = -1000, 1000

	count := make([]int, max-min+1)
	for _, x := range list {
		count[x-min]++
	}
	idx := 0
	for i, c := range count {
		for ; c > 0; c-- {
			list[idx] = i + min
			idx++
		}
	}
}
