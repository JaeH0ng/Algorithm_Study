import sys
from collections import deque

n = int(input())

A = []
B = []
C = []
queue = deque()

for _ in range(n):
    input_str = list(map(int, sys.stdin.readline().split()))
    if input_str[0] == 1:
        queue.append(input_str[1])
        queue.append(input_str[2])
    else:
        idx = queue.popleft()
        if queue.popleft() == input_str[1]:
            A.append(idx)
        else:
            B.append(idx)

if queue:
    C = [queue[i] for i in range(len(queue)) if i % 2 == 0]

A.sort()
B.sort()
C.sort()
'''
for a in A:
    print(a, end = ' ')
if not A:
    print("None")
print()
for b in B:
    print(b, end = ' ')
if not B:
    print("None")
print()
for c in C:
    print(c, end = ' ')
if not C:
    print("None")
'''
print(' '.join(map(str, A))) if A else print("None")
print(' '.join(map(str, B))) if B else print("None")
print(' '.join(map(str, C))) if C else print("None")

