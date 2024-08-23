populars=[[-1]*14 for _ in range(100000)]
populars[0]=[i for i in range(1,15)]

cases=int(input())

def dyn(floor,ho):
  if(populars[floor][ho-1]==-1):
    buffer=0
    for k in range(ho):
      buffer+=dyn(floor-1,k+1)
    populars[floor][ho-1]=buffer
    return populars[floor][ho-1]
  else:
    return populars[floor][ho-1]

    


for case in range(cases):
  floor=int(input())
  ho=int(input())
  print(dyn(floor,ho))

#112ms