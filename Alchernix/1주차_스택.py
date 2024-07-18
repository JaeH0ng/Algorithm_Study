import sys

N = int(input())

stack = []
for i in range(N):
    command = sys.stdin.readline().split() #input() 함수를 쓰면 시간초과
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        print(stack.pop()) if len(stack) != 0 else print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(1) if len(stack) == 0 else print(0)
    else:
        print(stack[-1]) if len(stack) != 0 else print(-1)
