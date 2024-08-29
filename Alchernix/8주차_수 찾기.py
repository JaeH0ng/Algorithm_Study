#160ms
N = int(input())
A = set(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if number in A:
        print(1)
    else:
        print(0)
