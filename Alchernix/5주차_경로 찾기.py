#처음 푼 풀이(시간 오래걸림)
import sys
from collections import deque

def bfs(i, j, N):
    visited = [j]
    queue = deque([(i, j)])
    is_edge[i][j] = 1
    while queue:
        y, x = queue.popleft()
        for k in range(N):
            if graph[x][k] and k not in visited:
                visited.append(k)
                queue.append((x, k))
                is_edge[i][k] = 1

N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
is_edge = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j]:
            bfs(i, j, N)

for i in range(N):
    for j in range(N):
        print(is_edge[i][j], end = ' ')
    print()


#다른 사람 풀이 참고
import sys
from collections import deque

def bfs(start):
    visited = [0] * N
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in range(N):
            if graph[v][i] and visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                is_edge[start][i] = 1
        
N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
is_edge = [[0] * N for _ in range(N)]

for i in range(N):
    bfs(i)

for i in range(N):
    for j in range(N):
        print(is_edge[i][j], end = ' ')
    print()
