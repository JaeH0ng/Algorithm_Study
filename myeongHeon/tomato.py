from collections import deque

# 인접 전파-bfs
grid = input().split()
cols = int(grid[0]) + 2
rows = int(grid[1]) + 2
boundary = 2 * (cols + rows) - 4

# 날짜/ 모두 시 0/ 불가시 -1
# 애초에 1이 여러 개인 경우도 생각.
# => 근데 그건 애초에 bfs가 그러지 않나?
# append 시 하루 지나고, 익는 처리로.
# x, y 축으로 0들을 enqueue 후 day++, 1 처리, count++. -1 시 리턴.
graph = []
bfsQue = deque()

# 입력 받으면서 bfs 위한 큐 준비
graph.append([-1] * cols)
for r in range(1, rows - 1):
    inputs = input().split()
    row = [-1]
    for i in range(cols - 2):
        value = int(inputs[i])
        row.append(value)
        if value == 1:
            # 큐에 시작 어펜드
            bfsQue.append({"row": r, "col": i + 1, "day": 0})
    row.append(-1)
    graph.append(row)
graph.append([-1] * cols)

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

date = dBfs(bfsQue, graph)
for row in graph:
    if 0 in row:
        date = -1
        break
print(date)

#1028초

