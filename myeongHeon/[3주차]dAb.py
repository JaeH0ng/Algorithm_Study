# class Node:
#   def __init__(self,number:int):
#     self.linked=list()
#     self.number=number

# 그래프 받아오기: 정점, 간선 정보 받기
from collections import deque
#onyl 끝지점 삽입삭제기에 환큐도 좋은데, 걍 덱은 c 구현이라서 쓰기로 함.

nums=input().split()
v=int(nums[0])
e=int(nums[1])
startNum=int(nums[2])  
# graphNodes=list(Node(i) for i in range(1,v+1))
graph={i: [] for i in range(1,v+1)}

for _ in range(e):
  pair=input().split()
  x=int(pair[0])
  y=int(pair[1])
  graph[x].append(y)
  graph[y].append(x)

#정점 번호 작게 방문하도록 링크 처리
sortedGraph={key: sorted(value) for key,value in graph.items()}

  
dfsVisitList=list()
def dfs(startNumber:int): 
  #방문에 추가
  dfsVisitList.append(startNumber)
  #작은 번호부터 방문하도록 하기
  for linkedNode in sortedGraph[startNumber]:
    if(linkedNode not in dfsVisitList):
      dfs(linkedNode)
    
dfs(startNum)
print(" ".join(map(str, dfsVisitList)))

bfsQue=deque()
bfsVisitList=list()
def bfs(startNumber:int):
  #큐에 삽입 및 방문 처리
  bfsQue.append(startNumber)
  bfsVisitList.append(startNumber)
  while(bfsQue):
    #왼쪽에서 빼고, 방문 처리하고, 뺀 거 필터링 후, 다시 추가
    poped= bfsQue.popleft()
    for node in sortedGraph[poped]:
      if node not in bfsVisitList:
        bfsQue.append(node)
        bfsVisitList.append(node)
bfs(startNum)
print(" ".join(map(str,bfsVisitList)))


# 192초
