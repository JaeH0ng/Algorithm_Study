#96ms
import sys

N = int(sys.stdin.readline().rstrip())
road = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

total = 0
minCost = cost[0]
for i in range(N - 1):
    if minCost > cost[i]:
        minCost = cost[i]
    total += minCost * road[i]
print(total)
