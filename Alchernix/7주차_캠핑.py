#32ms
import sys

L, P, V = map(int, sys.stdin.readline().split())
c = 1
while not L == P == V == 0:
    if L <= (V % P):
        day = ( L * (V // P) ) + ( L )
    else:
        day = ( L * (V // P) ) + ( (V % P) % L )
    print(f'Case {c}: {day}')
    L, P, V = map(int, sys.stdin.readline().split())
    c += 1
