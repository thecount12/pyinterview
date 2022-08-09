package main

import "fmt"

func main() {
	dataList := []int{1, 2, 3, 3, 4, 5}
	myMap := make(map[int]int)
	for i := 0; i < len(dataList); i++ {
		fmt.Println(dataList[i])
		item, found := myMap[dataList[i]]
		if !found {
			fmt.Println("its not int the list lets add")
			myMap[dataList[i]] = 1
		} else {
			fmt.Println("in list lets increment: ", item)
			myMap[dataList[i]] += 1
		}
	}
	fmt.Println(myMap)
	
}
