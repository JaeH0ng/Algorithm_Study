#최대 힙을 이용한 풀이(52ms)
'''
import sys
import heapq

N = int(input())

dasom = -int(sys.stdin.readline().rstrip()) #최대 힙을 이용하기 위해 부호를 바꿈
heap = []
for _ in range(N - 1):
    heapq.heappush(heap, -int(sys.stdin.readline().rstrip())) #다솜을 제외한 나머지 득표수로 힙 만들기
count = 0

if heap: #지원자가 다솜 1명밖에 없을 경우에 대비해 힙이 있는지 확인
    while heap[0] <= dasom: #가장 많은 득표수가 다솜의 득표수보다 많거나 같을 동안
        heapq.heappush(heap, heapq.heappop(heap) + 1) #가장 많은 득표수에서 1을 빼고 다시 힙에 넣는다
        dasom -= 1
        count += 1

print(count)
'''
#힙을 사용하지 않은 풀이(44ms)
import sys

N = int(input())

dasom = int(sys.stdin.readline().rstrip())
C = [int(sys.stdin.readline().rstrip()) for _ in range(N - 1)]
count = 0

if C:
    while dasom <= max(C): #가장 많은 득표수가 다솜의 득표수보다 많거나 같을 동안
        C[C.index(max(C))] -= 1 #가장 많은 득표수에서 1을 뺀다
        dasom += 1
        count += 1

print(count)
