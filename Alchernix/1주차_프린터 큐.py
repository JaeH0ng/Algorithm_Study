import sys
from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    papers = deque(map(int, sys.stdin.readline().split()))
    idx = deque([0 if i != M else 1 for i in range(N)])

    popped = cnt = 0

    while popped != 1:
        max_imp = max(papers)
        if max_imp > papers[0]:
            papers.append(papers.popleft())
            idx.append(idx.popleft())
        else:
            papers.popleft()
            popped = idx.popleft()
            cnt += 1
    print(cnt)
