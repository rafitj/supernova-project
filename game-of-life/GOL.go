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
	"sync"
)

// Grid world
type Grid struct {
	size       int
	numThreads int
	world      [][]int
}

func newGrid(size int, numThreads int) *Grid {
	grid := Grid{size: size, numThreads: numThreads}
	grid.createWorld()
	return &grid
}

func (grid *Grid) createWorld() {
	n := grid.size
	grid.world = make([][]int, n)
	for i := 0; i < n; i++ {
		grid.world[i] = make([]int, n)
	}
}

func main() {
	mux := sync.Mutex{}
	fmt.Println(mux)
	fmt.Println(newGrid(5, 1))
}
