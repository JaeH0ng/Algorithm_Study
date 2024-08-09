import sys

n = int(sys.stdin.readline().rstrip())

S = set()
for _ in range(n):
    log = sys.stdin.readline().split()
    if log[1] == 'enter':
        S.add(log[0])
    else:
        S.remove(log[0])

name_list = sorted(list(S), reverse=True)
print('\n'.join(name_list))
