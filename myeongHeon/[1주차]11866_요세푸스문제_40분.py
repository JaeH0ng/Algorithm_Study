#최대한 다양한 풀이 시도해 봤습니다
# 근데 그냥 푼 풀이가 젤 빠르던데.

# class CQueue:
#   def __init__(self,size):
#     self.size=size
#     self.front=0
#     self.rear=0
#     self.data_list=[None]*size
#     !self.count=0
#   #! count를 도입해서 그냥 큐 다 채울 수 있도록 함
#   #! 공백/ 다 참 구분을 수로 하기.
#   def enqueue(self, data):
#     !if(self.count==self.size):
#       print('it is full')
#       return 0
#     self.data_list[self.rear]=data
#     self.rear=(self.rear+1)%(self.size)
#     self.count+=1
#     return True
#   def dequeue(self):
#     !if(self.count==0):
#       print('it is empty')
#       return 0
#     self.data_list[self.front]=None
#     self.front=(self.front+1)%(self.size)
#     self.count-=1
#     return True




# import sys

# # 입력 받기
# n, k = map(int, sys.stdin.readline().split())

# idx = 0
# queue = [i for i in range(1, n+1)]
# res = []
# while queue:
#     idx += k - 1 
#     if idx >= len(queue):  
#         idx %= len(queue)  
#!    res.append(str(queue.pop(idx)))  # k번째 수 제거 후 결과 배열에 추가. 중간 pop시 그냥 배열 사용이 간편.

# # 결과 출력
# print("<", ", ".join(res), ">", sep="")




#! 중간에 있는걸 처리할땐 그냥 큐가 더 좋음.
#!일반 배열이 아닌 환큐 사용 이유: 수정이 빈번한 경우 그 시간복잡도를 크게 줄일 수 있음.
# !단, 모든 큐는 중간이 제거되는 경우에 취약하다. 수정이 한정적임. 프론트가 띄엄띄엄 되면 줄 잘림. 환큐는 원이 아니다.
#! 환큐는 진짜 원이 아니라, 그냥 게이트의 이동으로 처리하는 직선의 트릭 형태
#! 진짜 원으로 처리하려면 그냥 배열로 팝.
class TQueue:
  #k 단위로 빠지도록 설정
  def __init__(self,size,k):
    self.size=size
    self.front=-1
    self.k=k
    self.rear=0
    self.data_list=[None]*size
    self.count=0
  def enqueue(self, data):
    if(self.count==self.size):
      print('it is full')
      return 0
    self.data_list[self.rear]=data
    self.rear=(self.rear+1)%(self.size)
    self.count+=1
    return True
  def dequeueAndPop(self):
    if(self.count==0):
      return 0

    spin=self.k
    while(spin>0):
        #None 건너뛰어야 함.
        #그러나 del을 쓸 수는 없음. (del 자체가 시복이 큼) 
        self.front=(self.front+1)%self.size
        if(self.data_list[self.front]!=None):
          spin-=1
    target= self.data_list[self.front]
    self.data_list[self.front]=None
    self.count-=1
    return str(target)

strs=input()
strs=strs.split(' ')
n=int(strs[0])
k=int(strs[1])
circle=TQueue(n,k)
for i in range(n):
  circle.enqueue(i+1)
#생성
nums=[]
while(True):
  number=circle.dequeueAndPop()
  if(number==0):
    break
  nums.append(number)
numStr=", ".join(nums)
print("<"+numStr+">")