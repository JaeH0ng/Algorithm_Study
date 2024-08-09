# leaf의 정의가 차수
# 특수한 경우여도 됨.
# 어차피 간선 수는 정해짐 (node의 수 -1개)(1/0에서 +1)
# 그러므로 시간복잡도 크게 고려할 필요 없음
# 간선 수 고정, 알고리즘 시간복잡도는 n이하로 떨어지는게 불가하기 때문. 걍 n으로 쓰면 그게 최선임.

nums=input().split(" ")
n=int(nums[0])
m=int(nums[1])
k=n-m #inner의 수

# leaf를 m-1개, inner k개, 다시 1개
#idx는 0 ~ m-2/ m-1~ n+k-2/ n+k-1
for i in range(0,m-1):
  print(i,m-1)
for i in range(m-1, m+k-1):
  print(i, (i+1))
#시간: 40ms
