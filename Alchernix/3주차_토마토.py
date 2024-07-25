import sys
from collections import deque

def bfs(queue):
    while queue:
        x, y = queue.popleft()
        directions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for check_x, check_y in directions:
            if check_x < 0 or check_x >= M or check_y < 0 or check_y >= N:
                continue
            if matrix[check_y][check_x] == 0:
                if day[check_y][check_x] == -1 or day[check_y][check_x] > day[y][x] + 1:
                    day[check_y][check_x] = day[y][x] + 1
                matrix[check_y][check_x] = -1
                queue.append((check_x, check_y))
    
M, N = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
day = [[-1]*M for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if matrix[i][j] == -1:
            day[i][j] = 0
        if matrix[i][j] == 1:
            queue.append((j, i))
            matrix[i][j] = -1
            day[i][j] = 0
bfs(queue)

max_day = 0
check = 0
for i in range(N):
    for j in range(M):
        if day[i][j] > max_day:
            max_day = day[i][j]
        if day[i][j] == -1:
            check = -1
            
if check == -1:
    print(-1)
else:
    print(max_day)

