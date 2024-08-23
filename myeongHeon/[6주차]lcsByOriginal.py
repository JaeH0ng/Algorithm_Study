#그냥이 더 편하긴 한듯
#최소편집거리는 가능하긴 한데, 고려할게 많음
#lcs는 그중 보존성만 유지하면 끝이라

def lcs(s1,s2):
  m=len(s1)
  n=len(s2)
  dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
  for y in range(m+1):
    for x in range(n+1):
      if(y==0):
          dp[y][x]=0
      elif(x==0):
          dp[y][x]=0
      elif(s1[y-1]==s2[x-1]):
        #대각선 경우는 if가 필요없음. 경우 갈라봐도 무조건임. 무조건 +1
        dp[y][x]=1+dp[y-1][x-1]
      else:
        #다른 경우엔 전이. 전이 시 보존성 따라 최대로 픽.
        dp[y][x]=max(dp[y][x-1],dp[y-1][x])
  return dp[m][n]
        

s1=input()
s2=input()



print(lcs(s1,s2))
#124