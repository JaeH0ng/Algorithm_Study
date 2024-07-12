#스택 안 쓴 풀이
'''
import sys

N = int(input())
sticks = [int(sys.stdin.readline().rstrip()) for i in range(N)]

cnt = 1
tallest = sticks[-1]
for stick in sticks[::-1]:
    if stick > tallest:
        tallest = stick
        cnt += 1

print(cnt)
'''

#스택으로 풀이한 것
import sys
N = int(input())

sticks = []
for i in range(N):
    stick = int(sys.stdin.readline().rstrip())
    while sticks and sticks[-1] <= stick:
        sticks.pop()
    sticks.append(stick)

print(len(sticks))
