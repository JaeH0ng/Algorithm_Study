#풀이 1 코드는 더러운데 시간은 적게 걸림
#200ms
N, M = map(int, input().split())
lessons = list(map(int, input().split()))

start = max(lessons)
end =  sum(lessons)

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2 #블루레이의 크기
        result = mid
        cnt = get_cnt(mid)
        if cnt == M and get_cnt(mid - 1) > M:
            return result
        elif cnt > M:
            start = mid + 1
        else:
            end = mid - 1
    return result

def get_cnt(mid):
    cnt = 0
    blueray = 0
    for lesson in lessons:
        if lesson > mid:
            cnt = M + 1
            break
        blueray += lesson
        if blueray > mid:
            cnt += 1
            blueray = 0
            blueray += lesson
    cnt += 1
    return cnt
        
print(binary_search(start, end))

#풀이 2 코드는 비교적  깔끔한데 시간은 오래 걸림
#380ms
N, M = map(int, input().split())
lessons = list(map(int, input().split()))

start = max(lessons)
end = sum(lessons) 

while start <= end:
    mid = (start + end) // 2 #블루레이의 크기
    cnt = 0
    blueray = 0
    for lesson in lessons:
        blueray += lesson
        if blueray > mid:
            cnt += 1
            blueray = 0
            blueray += lesson
    cnt += 1
    #print(start, mid, end, cnt)
    if cnt > M:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)
