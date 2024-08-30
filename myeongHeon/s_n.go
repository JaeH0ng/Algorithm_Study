package main

import (
	"fmt"
	"math"
)

var uptoSN = map[int]int{}



func countPartialSN(lPlusOne, rightEnd int) int {
	if (rightEnd - lPlusOne + 1) <= 100000000 { // 작은 구간 처리
		isSN := make([]bool, rightEnd-lPlusOne+1)
		for i := 2; i <= int(math.Sqrt(float64(rightEnd))); i++ {
			square := i * i
			start := max(square, (lPlusOne+square-1)/square*square)
			for j := start; j <= rightEnd; j += square {
				isSN[j-lPlusOne] = true
			}
		}
		partialSN := 0
		for _, v := range isSN {
			if v {
				partialSN++
			}
		}
		totalSN := uptoSN[lPlusOne-1] + partialSN
		uptoSN[rightEnd] = totalSN

		for i := len(isSN) - 1; i >= 0; i-- {
			if !isSN[i] {
				return lPlusOne + i
			}
		}
	} else { // 큰 구간 처리
		chunkSize := (rightEnd-lPlusOne+1)/10 + 1
		maxSquareRoot := int(math.Sqrt(float64(rightEnd)))
		var lastSquareFree int

		for chunkStart := lPlusOne; chunkStart <= rightEnd; chunkStart += chunkSize {
			chunkEnd := min(chunkStart+chunkSize-1, rightEnd)
			isSN := make([]bool, chunkEnd-chunkStart+1)

			for i := 2; i <= maxSquareRoot; i++ {
				square := i * i
				start := max(square, (chunkStart+square-1)/square*square)
				for j := start; j <= chunkEnd; j += square {
					isSN[j-chunkStart] = true
				}
			}

			partialSN := 0
			for _, v := range isSN {
				if v {
					partialSN++
				}
			}
			totalSN := uptoSN[chunkStart-1] + partialSN
			uptoSN[chunkEnd] = totalSN

			for i := len(isSN) - 1; i >= 0; i-- {
				if !isSN[i] {
					lastSquareFree = chunkStart + i
				}
			}
		}
		return lastSquareFree
	}
	return -1
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var k int
	fmt.Scan(&k)

	countPartialSN(1, k)
	fnAns := k - uptoSN[k]

	if fnAns == k {
		fmt.Println(k)
	} else {
		l, r := k+1, 2*k
		for l <= r {
			m := (l + r) / 2
			temp := countPartialSN(l, m)
			upToSNM := uptoSN[m]

			fnM := m - upToSNM
			if fnM == k {
				fmt.Println(temp)
				break
			} else if fnM < k {
				l = m + 1
			} else {
				r = m - 1
			}
		}
	}
}
