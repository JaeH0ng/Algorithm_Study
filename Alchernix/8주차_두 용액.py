N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)

left = 0
right = len(arr) - 1
min_value = 1000000000
sol1 = None
sol2 = None

if arr[0] > 0:
    print(arr[0], arr[1])
elif arr[-1] < 0:
    print(arr[-2], arr[-1])
else:
    while left < right:
        if abs(arr[left] + arr[right]) < abs(min_value):
            min_value = arr[left] + arr[right]
            sol1, sol2 = arr[left], arr[right]
        if (arr[left] + arr[right]) > 0:
            right -= 1
        elif (arr[left] + arr[right]) < 0:
            left += 1
        else:
            sol1, sol2 = arr[left], arr[right]
            break
    print(sol1, sol2)
        
