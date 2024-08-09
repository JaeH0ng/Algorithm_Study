class MinHeap:
  def __init__(self):
    self.data=list()
    self.len=0
  def push(self, value):
    self.len+=1
    self.data.append(value)
    now_idx=self.len- 1
    while(now_idx>0):
      p_idx=(now_idx-1)//2 #t,k로 유도 가능
      if(p_idx<0):
        break
      if(self.data[p_idx]>self.data[now_idx]):
        (self.data[p_idx],self.data[now_idx])=(self.data[now_idx],self.data[p_idx])
        now_idx=p_idx
      else:
        break
  def pop (self):
    if(self.len==0):
      return None
    top=self.data[0]
    if(self.len==1):
      self.data.pop()
    else:
      self.data[0]=self.data.pop()
    self.len-=1
    now_idx=0
    while(True):
      left=now_idx*2+1
      right=left+1
      if(left>self.len-1):
        break
      minNum=self.data[left]
      minIdx=left
      if(right<self.len and self.data[right]<self.data[left]):
        minNum=self.data[right]
        minIdx=right
      if(self.data[now_idx]>minNum):
        (self.data[now_idx],self.data[minIdx])=(self.data[minIdx],self.data[now_idx])
        now_idx=minIdx
      else:
        break
    return top

heap=MinHeap()
n=int(input())
for i in range(n):
  num=int(input())
  if(num==0):
    top=heap.pop()
    print(top)
  else:
    heap.push(num)
# !시간 초과는 파이썬 자체 한계일지도.
# ! heapq는 c로 구현이라 더 빠르다고 함