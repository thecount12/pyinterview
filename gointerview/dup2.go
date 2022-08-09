// array = [1, 2, 3, 3, 4, 5, 6
// find duplicates, major and uniques]

package main

import "fmt"

func create(data []int) map[int]int {
	myHash := make(map[int]int)
	for i := 0; i < len(data); i++ {
		_, found := myHash[data[i]]
		if !found {
				myHash[data[i]] = 1
 		} else {
			myHash[data[i]] += 1
		}
	}
	return myHash
}

func check(c map[int]int) int {
	var myInt int
	for k, v := range c {
		if v > 1 {
			myInt = k
		}
	}
	return myInt
}

func main() {
	myArray := []int{1, 2, 3, 4, 5, 6}
	blah := create(myArray)
	found := check(blah)
	fmt.Println(found)
}
