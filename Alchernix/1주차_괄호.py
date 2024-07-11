import sys

def check_ps(ps):
    stack = []
    p_list = str(ps)
    for p in p_list:
        if p == '(':
            stack.append(p)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                print('NO')
                return
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

T = int(input())

for i in range(T):
    ps = sys.stdin.readline().rstrip()
    check_ps(ps)
