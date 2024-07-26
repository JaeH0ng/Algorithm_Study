import sys

def dfs(graph, v, visited = []):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            dfs(graph, w, visited)
    return visited

def bfs(graph, start_v):
    visited = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
for v_list in graph:
    v_list.sort()

print(' '.join(map(str, dfs(graph, V))))
print(' '.join(map(str, bfs(graph, V))))
