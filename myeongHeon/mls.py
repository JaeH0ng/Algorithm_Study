def bUpdateIdx(e):
    l = 0
    r = len(ml) - 1
    while l <= r:
        m = (l + r) // 2
        if ml[m] == e:
            return None
        elif ml[m] > e:
            r = m - 1
        else:
            l = m + 1
    return l

def mls():
    ml.append(numList[0])
    idxLastList[0] = 0
    idxToidx[0] = -1
    for idx in range(1, n):
        if numList[idx] > ml[-1]:
            ml.append(numList[idx])
            idxLastList[len(ml) - 1] = idx
            idxToidx[idx] = idxLastList[len(ml) - 2]
        else:
            changeIdx = bUpdateIdx(numList[idx])
            if changeIdx is not None:
                ml[changeIdx] = numList[idx]
                idxLastList[changeIdx] = idx
                if changeIdx > 0:
                    idxToidx[idx] = idxLastList[changeIdx - 1]
                else:
                    idxToidx[idx] = -1

n = int(input())
numList = list(map(int, input().split()))
ml = []

idxLastList = [-1] * n
idxToidx = [-1] * n

mls()


ans = []
currentIdx = idxLastList[len(ml) - 1]
while currentIdx != -1:
    ans.append(numList[currentIdx])
    currentIdx = idxToidx[currentIdx]

print(len(ans))
print(' '.join(map(str, ans[::-1])))
