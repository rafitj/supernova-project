package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

var (
	wg sync.WaitGroup
)

func main() {

}

type MatrixValue struct {
	value int
	i     int
	j     int
}

func createRandomMatrix(rows int, cols int) [][]int {
	matrix := make([][]int, rows)
	for i := 0; i < rows; i++ {
		matrix[i] = make([]int, cols)
		for j := 0; j < cols; j++ {
			matrix[i][j] = rand.Intn(100)
		}
	}
	return matrix
}

func multiplyMatrix() {
	start := time.Now()

	c := make(chan MatrixValue)
	matrixA := createRandomMatrix(3, 3)
	matrixB := createRandomMatrix(3, 3)

	fmt.Println(matrixA, matrixB)

	for i, rowA := range matrixA {
		go row()
		for j := range matrixB[0] {
			var col []int
			for z := range matrixB {
				col = append(col, matrixB[z][j])
			}
			wg.Add(1)
			go dotProduct(rowA, col, i, j, c)
		}
	}

	matrixC := make([][]int, len(matrixA))
	for i := range matrixC {
		matrixC[i] = make([]int, len(matrixB[0]))
	}

	wg.Wait()
	close(c)

	for v := range c {
		x := v
		matrixC[x.i][x.j] = x.value
	}
	fmt.Println(matrixC)
	t := time.Now()
	elapsed := t.Sub(start)
	fmt.Println(elapsed)
	return matrixC
}

func dotProduct(a1 []int, a2 []int, i int, j int, c chan MatrixValue) {
	defer wg.Done()

	var ans []int
	for i, a := range a1 {
		ans = append(ans, a*a2[i])
	}
	c <- MatrixValue{sum(ans), i, j}
}

func sum(nums []int) int {
	total := 0
	for _, num := range nums {
		total += num
	}
	return total
}
