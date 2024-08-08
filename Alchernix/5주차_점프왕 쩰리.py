#32ms
import sys

def dfs(y, x):
    visited[y][x] = 1
    move = [(x + matrix[y][x], y), (x, y + matrix[y][x])]
    for checkX, checkY in move:
        if checkY < 0 or checkY >= N or checkX < 0 or checkX >= N:
            continue
        if visited[checkY][checkX] == 0:
            dfs(checkY, checkX)
    

N = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dfs(0, 0)

if visited[N - 1][N - 1] == 1:
    print("HaruHaru")
else:
    print("Hing")
