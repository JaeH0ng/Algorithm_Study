t=int(input())
p=((2*t)**(1/2))-1
int_p=int(p)
plus_p=int_p+1
if(p==int_p):
# 결국 붎필요긴 해도, 논리적으론 이게 먼저 유도.
  print(int_p)
elif((plus_p**2+plus_p)<=2*t):
# 큰 경우 우선 검토
  print(plus_p)
else:
# 불가 시 작은거.
  print(int_p)