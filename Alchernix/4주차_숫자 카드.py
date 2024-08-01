N = int(input())
cards = set(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if number in cards:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
