#32ms
import sys

T = int(sys.stdin.readline().rstrip())
fact = [1] * 31
for i in range(2, 31):
    fact[i] = fact[i - 1] * i
    
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(fact[M] // (fact[M - N] * fact[N]))
