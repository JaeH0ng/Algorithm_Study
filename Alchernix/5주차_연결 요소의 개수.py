#612ms

import sys
from collections import deque

def bfs(start_v):
    queue = deque([start_v])
    visited[start_v] = 1
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if visited[w] == 0:
                visited[w] = 1
                queue.append(w)
    return 1

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)
cnt = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        cnt += bfs(i)
print(cnt)
