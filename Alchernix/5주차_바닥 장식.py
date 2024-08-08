#40ms
import sys

N, M = map(int, sys.stdin.readline().split())

floor = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
cnt = 0

for i in range(N): 
    for j in range(M): 
        if floor[i][j] == '-':
            floor[i][j] = 0
            k = j + 1
            while k < M and floor[i][k] == '-':
                floor[i][k] = 0
                k += 1
            cnt += 1
        elif floor[i][j] == '|':
            floor[i][j] = 0
            k = i + 1
            while k < N and floor[k][j] == '|':
                floor[k][j] = 0
                k += 1
            cnt += 1
print(cnt)
