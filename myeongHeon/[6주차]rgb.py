n=int(input())
dyn=[[-1]*3 for i in range(n+1)]

houseCost=[[-1]*3 for i in range(n+1)]

for house in range(1,n+1):
  (r,g,b)=input().split()
  houseCost[house][0]=int(r)
  houseCost[house][1]=int(g)
  houseCost[house][2]=int(b)
dyn[1]=houseCost[1]


def minify(k):
  if(dyn[k][0] != -1):
    return min(dyn[k])
  else:
    dyn[k][0]=min(dyn[k-1][1]+houseCost[k][0], dyn[k-1][2]+houseCost[k][0])
    dyn[k][1]=min(dyn[k-1][0]+houseCost[k][1], dyn[k-1][2]+houseCost[k][1])
    dyn[k][2]=min(dyn[k-1][0]+houseCost[k][2], dyn[k-1][1]+houseCost[k][2])

for i in range(1,n+1):
  minify(i)
print(minify(n))

#100ms
