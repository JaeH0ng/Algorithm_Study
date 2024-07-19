import sys
import heapq

heap = []
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x > 0:
        heapq.heappush(heap, x)
    elif heap:
        print(heapq.heappop(heap))
    else:
        print(0)
