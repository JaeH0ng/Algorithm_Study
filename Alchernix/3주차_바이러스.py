import sys

def dfs(graph, v, visited = []):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            dfs(graph, w, visited)
    return visited

C = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(C+1)]

for _ in range(P):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

print(len(dfs(graph, 1)) - 1)
