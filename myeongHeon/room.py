n = int(input())

info = []
for _ in range(n):
    s, e = input().split()
    info.append([int(e), int(s)])  # 종료 시간(e)을 먼저, 시작 시간(s)을 나중에 추가
info.sort()  # 종료 시간 기준으로 정렬

lineTime = 0
count = 0
lineIdx=0

# 정렬된 리스트를 순회하면서 조건을 만족하는 스케줄 선택
for idx, (endTime, startTime) in enumerate(info[lineIdx:], start=lineIdx):
    if startTime >= lineTime:  # 현재 스케줄이 가능하다면
        lineTime = endTime  # 종료 시간을 업데이트
        count += 1  # 선택한 스케줄의 수 증가
        lineIdx=idx+1

print(count)
