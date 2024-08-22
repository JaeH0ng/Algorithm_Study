#52ms
S = int(input())

for i in range(1, S + 1):
    if i * (i + 1) // 2 > S:
        break
print(i - 1) if S != 1 else print(1)
