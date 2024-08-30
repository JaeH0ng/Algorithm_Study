from collections import deque

(y, x) =list(map(int,input().split()))

prison=list()
for i in range(y):
  row=input()
  prison.append(list(row))
print(prison)

#* 1. bfs로 "거리", "예상 대기시간" 구한 후, 이분매칭으로 우선순위 가장 가까운 놈부터?
# ? 근데 이진 탐색이 어캐 사용됨?
#? 여기의 문제가 뭘까? 병목현상이려나?

bfsQue = deque()

def dBfs(bfsQue, graph):
    poped = -1
    while bfsQue:
        poped = bfsQue.popleft()
        if graph[poped["row"] - 1][poped["col"]] == 0:
            graph[poped["row"] - 1][poped["col"]] = 1
            bfsQue.append({"row": poped["row"] - 1, "col": poped["col"], "day": poped["day"] + 1})
        if graph[poped["row"] + 1][poped["col"]] == 0:
            graph[poped["row"] + 1][poped["col"]] = 1
            bfsQue.append({"row": poped["row"] + 1, "col": poped["col"], "day": poped["day"] + 1})
        if graph[poped["row"]][poped["col"] - 1] == 0:
            graph[poped["row"]][poped["col"] - 1] = 1
            bfsQue.append({"row": poped["row"], "col": poped["col"] - 1, "day": poped["day"] + 1})
        if graph[poped["row"]][poped["col"] + 1] == 0:
            graph[poped["row"]][poped["col"] + 1] = 1
            bfsQue.append({"row": poped["row"], "col": poped["col"] + 1, "day": poped["day"] + 1})
    return poped["day"] if poped != -1 else 0
