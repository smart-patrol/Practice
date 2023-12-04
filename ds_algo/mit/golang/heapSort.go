package main

import (
	"container/heap"
	"fmt"
)

//https://www.sohamkamani.com/golang/heap/

func main() {
	// create a new intHeap instance
	nums := &intHeap{3, 1, 4, 5, 1, 1, 2, 6}
	// The `Init` function reorders the numbers into a heap
	heap.Init(nums)
	fmt.Println(nums)
}

// since we need to define methods on the type to implement the heap interface
type intHeap []int

// Len is the number of elements in the collection.
func (h intHeap) Len() int {
	return len(h)
}

// Less reports whether the element with index i
// must sort before the element with index j.
// This will determine whether the heap is a min heap or a max heap
func (h intHeap) Less(i int, j int) bool {
	return h[i] < h[j]
}

// Swap swaps the elements with indexes i and j.
func (h intHeap) Swap(i int, j int) {
	h[i], h[j] = h[j], h[i]
}

// Push and Pop are used to append and remove the last element of the slice
func (h *intHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *intHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}
