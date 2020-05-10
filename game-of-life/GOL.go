/*
	Design Conway’s Game of Life using an n x n grid.
	It should be configurable to run with 1+ threads. When there are 2 or more threads,
	the grid should be sectioned off such that each thread updates a specific region of
	the board. In this way, synchronization will largely be unnecessary except on the boundaries
	where one thread’s section crosses over into another thread’s section. When a thread
	completes one iteration of an update, it should wait until the control thread signals
	that it’s ok to start the next iteration (this way, all threads are all working on the same time step).
	This should display a very simple, 2D cell-based grid to show the board as it changes at each update.

	Rules:
	Organisims can be alive (1) or dead (0)
	The neighbours of an organism are the 8 cells around it
	1) If an organism is surrounded by 4+ organisms, it dies
	2) If an organism is surrounded by 1- organisims, it dies
	3) If an empty cell is surrounded by exactly 3 organisims, it gives life
*/

package main

import (
	"fmt"
	"math/rand"
	"sync"
)

type Thread struct {
	threadNum    int
	grid         Grid
	lock         sync.Mutex
	area         [][]int
	iterComplete bool
}
type Grid struct {
	size       int
	numThreads int
	world      [][]int
	threads    []*Thread
}

func newGrid(size int, numThreads int) *Grid {
	grid := Grid{size: size, numThreads: numThreads}
	grid.createWorld()
	grid.threads = make([]*Thread, 0)
	batchSize := size / numThreads
	for i := 0; i < numThreads; i++ {
		start := i * batchSize
		end := start + batchSize
		newThread := Thread{i, grid, sync.Mutex{}, grid.world[start:end][:]}
		if i == numThreads-1 {
			newThread = Thread{i, grid, sync.Mutex{}, grid.world[start:len(grid.world)][:]}
		}
		grid.threads = append(grid.threads, &newThread)
	}
	return &grid
}

func (grid *Grid) randomPopulate() {
	for r, row := range grid.world {
		for c := range row {
			if rand.Float32() > 0.3 {
				grid.world[r][c] = 0
			} else {
				grid.world[r][c] = 1
			}

		}
	}
}

func (thread *Thread) checkCell(i int, j int) int {
	if i < 0 || j < 0 || i >= thread.grid.size || j >= thread.grid.size {
		return 0
	}
	return thread.grid.world[i][j]
}

func (thread *Thread) countSurrounding(i int, j int) int {
	count := 0
	count += thread.checkCell(i+1, j) + thread.checkCell(i+1, j+1) + thread.checkCell(i, j+1) + thread.checkCell(i-1, j+1)
	count += thread.checkCell(i-1, j) + thread.checkCell(i-1, j-1) + thread.checkCell(i, j-1) + thread.checkCell(i+1, j-1)
	return count
}

func (thread *Thread) updateCell(i int, j int) {
	count := thread.countSurrounding(i, j)
	if thread.area[i][j] == 1 && (count > 3 || count < 2) {
		thread.grid.world[i][j] = 0
	}
	if thread.area[i][j] == 0 && count == 3 {
		thread.grid.world[i][j] = 1
	}
}

func (thread *Thread) iterate() {
	for i := range thread.area {
		for j := range thread.area[i] {
			thread.updateCell(i, j)
		}
	}
}

func (grid *Grid) createWorld() {
	n := grid.size
	grid.world = make([][]int, n)
	for i := 0; i < n; i++ {
		grid.world[i] = make([]int, n)
	}
	grid.randomPopulate()
}

func main() {
	fmt.Println(newGrid(11, 5))
}
