from collections import deque

def bfs(graph, startNumber: int, k: int):
    bfsQue = deque()
    bfsVisitList = [0]*(len(graph)+1)
    #1~이므로
    bfsQue.append([startNumber, 0])
    bfsVisitList[startNumber]=1
    flag = True
    
    
    while bfsQue:
        poped = bfsQue.popleft()
        current_node = poped[0]
        current_distance = poped[1]
        
        if current_distance == k:
            print(current_node)
            flag = False
        
        for node in graph[current_node]:
            if bfsVisitList[node]==0:
                bfsQue.append([node, current_distance + 1])
                bfsVisitList[node]=1
    
    if flag:
        print(-1)

nums = input().split()
# N, M, K, X
N = int(nums[0])
M = int(nums[1])
K = int(nums[2])
X = int(nums[3])

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    edge = input().split()
    graph[int(edge[0])].append(int(edge[1]))

for key in graph:
    graph[key].sort()

bfs(graph, X, K)
