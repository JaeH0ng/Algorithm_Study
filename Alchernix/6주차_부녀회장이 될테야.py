#40ms
import sys

def resident(k, n):
    table = [[0]*n for _ in range(k + 1)]
    for i in range(n):
        table[0][i] = i + 1
    for i in range(1, k + 1):
        for j in range(n):
            table[i][j] = sum(table[i - 1][:j + 1])
    return table[k][n - 1]
        
    

T = int(input())

for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    print(resident(k, n))
