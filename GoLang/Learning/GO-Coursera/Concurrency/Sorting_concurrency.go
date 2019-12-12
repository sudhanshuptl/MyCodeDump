package main

import (
	"fmt"
	"sort"
	"sync"
)

func sortArray(slc []int, wd *sync.WaitGroup) {
	fmt.Println("Subarray to sort : ", slc)
	sort.Ints(slc)
	wd.Done()
}

func mergeSort(slc []int, wd *sync.WaitGroup, mainWd *sync.WaitGroup) {
	wd.Wait()
	sort.Ints(slc)
	mainWd.Done()
}

func main() {
	var n, v, i int
	var wd, mainWd sync.WaitGroup
	for {
		fmt.Print("Enter Number of element to sort:> ")
		_, _ = fmt.Scan(&n)
		if n < 4 {
			fmt.Println("n must be greater than equal to 4")
		} else {
			break
		}
	}
	arr := make([]int, n)
	fmt.Print("Enter array elements :> ")
	for i = 0; i < n; i++ {
		_, _ = fmt.Scan(&v)
		arr[i] = v
	}

	fmt.Println(arr)
	//split in 4
	v = int(n / 4)
	wd.Add(1)
	go sortArray(arr[:v], &wd)
	wd.Add(1)
	go sortArray(arr[v:v*2], &wd)
	wd.Add(1)
	go sortArray(arr[v*2:v*3], &wd)
	wd.Add(1)
	go sortArray(arr[v*3:], &wd)

	mainWd.Add(1)
	go mergeSort(arr[:], &wd, &mainWd)
	mainWd.Wait()
	fmt.Println("Complete sorted array :> ", arr)

}
