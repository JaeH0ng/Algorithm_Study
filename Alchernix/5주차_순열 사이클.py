#520ms

import sys

def dfs(v):
    visited[v] = 1
    for w in graph[v]:
        if visited[w] == 0:
            dfs(w)

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(N + 1)]
    arr1 = list(range(1, N + 1))
    arr2 = list(map(int, sys.stdin.readline().split()))

    for v1, v2 in zip(arr1, arr2):
        if v1 != v2:
            graph[v1].append(v2)
            graph[v2].append(v1)
    visited = [0] * (N + 1)
    cnt = 0
    for v in range(1, N + 1):
        if visited[v] == 0:
            dfs(v)
            cnt += 1
    print(cnt)
    
