N, K = map(int, input().split())

def bfs(x):
    visited[x] = 1
    queue = [x]
    while queue:
        v = queue.pop(0)
        for w in [v - 1, v + 1, 2 * v]:
            if w < 0 or w >= len(visited):
                continue
            if visited[w] == 0:
                visited[w] = 1
                distance[w] = distance[v] + 1
                queue.append(w)
            if w==K:
                return
    
visited = [0] * 100001
distance = [0] * 100001
bfs(N)
print(distance[K])
