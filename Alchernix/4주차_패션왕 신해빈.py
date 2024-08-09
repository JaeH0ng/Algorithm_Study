import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    dic = dict()
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        name, wearclass = sys.stdin.readline().split()
        if wearclass in dic:
            dic[wearclass].append(name)
        else:
            dic[wearclass] = [name]
    c = 1
    for key, value in dic.items():
        c *= (len(value) + 1)
    print(c - 1)
