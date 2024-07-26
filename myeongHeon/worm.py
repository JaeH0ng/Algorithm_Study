from collections import deque
v=int(input())
e=int(input())
graph={i: [] for i in range(1,v+1)}
for _ in range(e):
  pair=input().split()
  x=int(pair[0])
  y=int(pair[1])
  graph[x].append(y)
  graph[y].append(x)

bfsQue=deque()
bfsVisitList=list()
def bfs(count:int, startNumber:int):
  #큐에 삽입 및 방문 처리
  bfsQue.append(startNumber)
  bfsVisitList.append(startNumber)
  while(bfsQue):
    #왼쪽에서 빼고, 방문 처리하고, 뺀 거 필터링 후, 다시 추가
    poped= bfsQue.popleft()
    for node in graph[poped]:
      if node not in bfsVisitList:
        bfsQue.append(node)
        count+=1
        bfsVisitList.append(node)
  return count
print(bfs(0,1))
#137ms