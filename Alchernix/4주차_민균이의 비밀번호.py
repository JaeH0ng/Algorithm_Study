import sys

N = int(sys.stdin.readline().rstrip())
lst = [sys.stdin.readline().rstrip() for _ in range(N)]

for password in lst:
    if password[::-1] in lst:
        print(len(password), password[len(password) // 2])
        break
