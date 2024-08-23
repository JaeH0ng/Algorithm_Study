a = input() #세로
b = input() #가로

table = [[0] * len(b) for _ in range(len(a))]

if a[0] == b[0]:
    table[0][0] = 1
for i in range(1, len(b)):
    table[0][i] = table[0][i - 1]
    if a[0] == b[i]:
        table[0][i] = 1
for j in range(1, len(a)):
    table[j][0] = table[j - 1][0]
    if a[j] == b[0]:
        table[j][0] = 1

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            table[i][j] = table[i - 1][j - 1] + 1
        else:
            table[i][j] = max(table[i][j - 1], table[i - 1][j])

print(table[len(a) - 1][len(b) - 1])
