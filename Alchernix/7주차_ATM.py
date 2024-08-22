#40ms
N = int(input())

time = list(map(int, input().split()))
time.sort()

time_sum = 0
for i in range(len(time)):
    time_sum += sum(time[:i+1])
print(time_sum)
