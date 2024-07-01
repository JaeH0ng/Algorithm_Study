'''
#처음 제출한 코드
first = int(input())
second = int(input())

print(first * (second % 10))
print(first * (second % 100 // 10))
print(first * (second // 100))
print(first * second)
'''

#다른 사람 풀이 참고한 것
first = int(input())
second = input()

for i in second[::-1]:
    print(first * int(i))
print(first * int(second))
