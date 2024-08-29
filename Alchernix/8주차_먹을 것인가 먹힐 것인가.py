#처음 푼 코드
#292ms
'''
import sys
T = int(sys.stdin.readline().rstrip())

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if B_list[mid] >= target and B_list[mid - 1] < target:
            return mid - 1
        elif B_list[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return mid

for _ in range(T):
    cnt = 0
    N, M = map(int, sys.stdin.readline().split())
    A_list = list(map(int, sys.stdin.readline().split()))
    A_list.sort()
    B_list = list(map(int, sys.stdin.readline().split()))
    B_list.append(0)
    B_list.sort()
    for A in A_list:
        cnt += binary_search(A, 1, len(B_list) - 1)
    print(cnt)
'''
#다른 사람 풀이 보고 개선한 것
#260ms
import sys
T = int(sys.stdin.readline().rstrip())

def binary_search(target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if B_list[mid] >= target:
            end = mid - 1
        else:
            result = mid #마지막으로 target보다 작을 때의 index를 저장
            start = mid + 1
    return result

for _ in range(T):
    cnt = 0
    N, M = map(int, sys.stdin.readline().split())
    A_list = list(map(int, sys.stdin.readline().split()))
    A_list.sort()
    B_list = list(map(int, sys.stdin.readline().split()))
    B_list.sort()
    for A in A_list:
        cnt += binary_search(A, 0, len(B_list) - 1) + 1
    print(cnt)
