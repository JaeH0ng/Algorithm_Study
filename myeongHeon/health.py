def solution(n, lost, reserve):
    temp=lost
    lost = set(lost) - set(reserve)
    reserve = set(reserve) - set(temp)    
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
    answer = n - len(lost)
    return answer
