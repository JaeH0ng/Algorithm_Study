import sys

def bfs(graph, start_y, start_x):
    queue = [(start_x, start_y)]
    graph[start_y][start_x] = 0

    while queue:
        x, y = queue.pop(0)
        
        directions = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        for checkX, checkY in directions:
            if checkX < 0 or checkX >= M or checkY < 0 or checkY >= N:
                continue
            if graph[checkY][checkX] == 1:
                graph[checkY][checkX] = 0
                queue.append((checkX, checkY))
            
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[Y][X] = 1
        
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    print(cnt)
