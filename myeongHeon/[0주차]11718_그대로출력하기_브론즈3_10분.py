import sys

input_data = []


while True:
    try:
        line = input()
        if line.strip() == "":
            break
        input_data.append(line)
    except EOFError:
        break

# 입력받은 데이터 처리
for line in input_data:
    print(line)
