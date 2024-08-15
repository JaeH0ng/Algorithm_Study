#36ms
N = int(input())

arr = [5000] * (N + 1)
arr[3] = 1
if N >= 5:
    arr[5] = 1
    for i in range(6, N + 1):
        arr[i] = min(arr[i - 3], arr[i - 5]) + 1
print(arr[N]) if arr[N] < 5000 else print(-1)
