
firstNum = int(input())
secondNum = input()

result = []

for digit in secondNum[::-1]:
    result.append(firstNum * int(digit))
result.append(result[0] + result[1] * 10 + result[2] * 100)

for res in result:
    print(res)
