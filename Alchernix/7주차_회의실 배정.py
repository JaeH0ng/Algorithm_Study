#252ms
import sys

N = int(sys.stdin.readline().rstrip())
tasks = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tasks.sort(key = lambda x : (x[1], x[0])) #일찍 끝나는 순서대로, 끝나는 시간이 같으면 일찍 시작하는 순서대로

done = tasks[0]
cnt = 1

for i in range(1, len(tasks)):
    s, f = done[0], done[1] #시작시간, 끝나는 시간
    if tasks[i][0] >= f: #f보다 늦게 시작하면
        done = tasks[i]
        cnt += 1

print(cnt)
