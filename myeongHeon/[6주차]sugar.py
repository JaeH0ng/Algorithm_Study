target=int(input())

minBongs=[-1]*5001
#미정 값은 -1로
minBongs[:5]=[float('inf')]*5
#0~4까지의 들 수 없는 값들은 무한대 처리. 
#추후에 7같은 놈들은 나중에 기록되게 되어 있음. 초기값만 설정.
minBongs[3]=1
minBongs[5]=1

def minify(target):
  if(minBongs[target]!=-1 or minBongs[target]==float('inf')):
    return minBongs[target]
  #종료 조건이 두 개임. 알거나, 계산 불가거나.
  else:
    minBongs[target]=min(minify(max(target-5,0))+1, minify(max(target-3,0))+1)
    #음수 방지
    return minBongs[target]
print(-1 if minify(target)==float('inf') else minify(target))

#100ms