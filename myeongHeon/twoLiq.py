n=int(input())
s_l=input().split()
n_l=list(map(int,s_l))
n_l.sort()
if(n_l[0]>0):
  print(n_l[0],n_l[1])
elif(n_l[-1]<0):
  print(n_l[-2],n_l[-1])
#이 경우까지가 벨런스 붕괴의 경우
# 벨런스가 있을 시엔, 그 지점까지만 조합
else:
  def bSearch (target):
    l=0
    r=len(n_l)-1
    ans={"flag":-1,"idx":-1}
    while(r>=l):
      m=(l+r)//2
      if(n_l[m]==target):
        ans["flag"]=1
        ans["idx"]=m
        break
      elif(n_l[m]<target):
        l=m+1
      else:
        r=m-1
    if(ans["flag"]==-1):
      l=r
      if(l==len(n_l)-1):
        l=l-1
      ans["idx"]=max(l,0)
    return ans
  minComb=list()
  flag=-1
  for n_idx,num in enumerate(n_l):
    #전부 순회 필요. 대칭성 성립 x임.
    reflectAns=bSearch(-num)
    if(reflectAns["flag"]==1 ):
      flag=1
      #답이 나옴 체크
      print(num, n_l[reflectAns["idx"]])
      break
    else:
      #답이 나오지 않은 경우
      l_idx=reflectAns["idx"]
      r_idx=reflectAns["idx"]+1
      if(l_idx==n_idx):
        l_idx=l_idx-1
        #여기서 바운더리 케이스는 자동으로 걸러짐
      if(r_idx==n_idx):
        r_idx=r_idx+1

      lh=0
      rh=0
      if(l_idx<0):
        lh=2000000001
      else:
        lh=num+n_l[l_idx]
      if(r_idx>len(n_l)-1):
        rh=2000000001
      else:
        rh=num+n_l[r_idx]      
      if(abs(lh)<=abs(rh)):
        minComb.append([abs(lh),num,n_l[l_idx]])
      else:
        minComb.append([abs(rh),num,n_l[r_idx]])
  if(flag!=1):
    endMinComb=min(minComb)
    print(endMinComb[1],endMinComb[2])

#176ms
#*회고하기. 오류처리!!
#*문제였던 것: not 핵심 로직, 다만, 핵심 로직의 "예외 처리 부분"에서 상당한 시간을 썼음