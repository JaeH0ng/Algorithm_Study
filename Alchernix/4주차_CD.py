import sys

N, M = map(int, sys.stdin.readline().split())
while N != 0 or M != 0:
    cnt = 0
    set_N = set([int(sys.stdin.readline().rstrip()) for _ in range(N)])
    for _ in range(M):
        cd = int(sys.stdin.readline().rstrip())
        if cd in set_N:
            cnt += 1
    print(cnt)
    N, M = map(int, sys.stdin.readline().split())
