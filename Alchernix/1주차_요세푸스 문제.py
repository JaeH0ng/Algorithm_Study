from collections import deque

N, K = map(int, input().split())


array = list(range(1, N + 1))

cnt = 1
idx = 0
print("<", end = '')
while array:
    if cnt % K == 0:
        print(array.pop(idx), end = ', ') if len(array) != 1 else print(array.pop(idx), end = '')
        idx -= 1
    cnt += 1
    idx += 1
    if idx == len(array):
        idx = 0

print(">", end = '')
