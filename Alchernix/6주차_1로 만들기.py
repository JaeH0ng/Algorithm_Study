#660ms
N = int(input())

table = {1:0, 2:1, 3:1}

for i in range(4, N + 1):
    if i % 3 == 0 and i % 2 == 0:
        table[i] = min(table[i // 3] + 1, table[i // 2] + 1, table[i - 1] + 1)
    elif i % 3 == 0:
        table[i] = min(table[i // 3] + 1, table[i - 1] + 1)
    elif i % 2 == 0:
        table[i] = min(table[i // 2] + 1, table[i - 1] + 1)
    else:
        table[i] = table[i - 1] + 1

print(table[N])
