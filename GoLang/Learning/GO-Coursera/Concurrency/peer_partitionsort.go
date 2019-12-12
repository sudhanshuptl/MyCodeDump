package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
	"sync"
)

func merge(left, right []int) (result []int) {
	result = make([]int, len(left)+len(right))

	i := 0
	for len(left) > 0 && len(right) > 0 {
		if left[0] < right[0] {
			result[i] = left[0]
			left = left[1:]
		} else {
			result[i] = right[0]
			right = right[1:]
		}
		i++
	}

	for j := 0; j < len(left); j++ {
		result[i] = left[j]
		i++
	}
	for j := 0; j < len(right); j++ {
		result[i] = right[j]
		i++
	}

	return
}

func sortInts(a []int, wg *sync.WaitGroup) {
	fmt.Println(a) // Each goroutine which sorts ¼ of the array should print the subarray that it will sort
	sort.Ints(a)
	if wg != nil {
		wg.Done()
	}
}

func sortBy4Routines(a []int) {
	var wg sync.WaitGroup

	n := len(a)
	m := n / 4
	carry := n % 4
	buckets := []int{m, 0, m, 0, m, 0, m, 0} //[low, high, low, high, ...]

	for i := 0; i < carry; i++ {
		buckets[i*2] += 1
	}

	start := 0
	for i := 0; i < 4; i++ {
		buckets[i*2+1] = start + buckets[i*2]
		buckets[i*2] = start
		start = buckets[i*2+1]
	}

	wg.Add(4)
	for i := 0; i < 4; i++ {
		go sortInts(a[buckets[i*2]:buckets[i*2+1]], &wg)
	}
	wg.Wait()

	x := merge(a[buckets[0]:buckets[1]], a[buckets[2]:buckets[3]])
	y := merge(a[buckets[4]:buckets[5]], a[buckets[6]:buckets[7]])

	fmt.Println(merge(x, y)) //When sorting is complete, the main goroutine should print the entire sorted list.
}

func main() {

	fmt.Println("Please input a series of integer with space delimiter:") //The program should prompt the user to input a series of integers
	scanner := bufio.NewScanner(os.Stdin)

	var input string
	if scanner.Scan() {
		input = scanner.Text()
	}

	// Convert input to integers
	fields := strings.Fields(input)
	n := len(fields)
	nums := make([]int, n)
	for i := 0; i < n; i++ {
		num, err := strconv.Atoi(fields[i])
		if err != nil {
			fmt.Println(err)
			os.Exit(-1)
		}
		nums[i] = num
	}

	// if the input len is less than 4, we sort them directly.
	// Otherwise we create 4 goroutines to sort each part and merge them together.
	if n >= 4 {
		sortBy4Routines(nums)
	} else {
		sortInts(nums, nil)
		fmt.Println(nums)
	}
}
