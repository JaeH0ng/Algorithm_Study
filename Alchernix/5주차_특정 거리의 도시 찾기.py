#1752ms
import sys
from collections import deque

def bfs(x, k):
    distance = [0] * (N + 1)
    visited[x] = 1
    queue = deque([x])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if visited[w] == 0:
                distance[w] = distance[v] + 1
                visited[w] = 1
                queue.append(w)
    return distance

N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    
visited = [0] * (N + 1)
distance = bfs(X, K)

answer = [str(i) for i in range(1, N + 1) if distance[i] == K ]
print('\n'.join(answer)) if answer else print(-1)
