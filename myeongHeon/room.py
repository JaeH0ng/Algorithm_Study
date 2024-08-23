n=int(input())

info=list()
for _ in range(n):
  (s,e)=input().split()
  info.append([int(s),int(e)])
info.sort()
for i in range(n):
# info에 몇등으로 시작하는지 기록
  info[i].append(i)
print(info)

lineIdx=0
count=0

while(True):
  endList=[[info[1],info[2]] for info in info[lineIdx+1:]]
  if not endList:
    break
  print(lineIdx,endList)
  endInfo=min(endList)
  print(endInfo)
  endTime=endInfo[0]
  lineIdx=endInfo[1]
  count+=1

print(count)