import math

def count_square_free_in_range(l, r):
    def count_square_free(n):
        # n 이하의 제곱ㄴㄴ수의 개수를 포함 배제의 원리를 사용하여 계산
        count = n
        limit = int(math.sqrt(n)) + 1
        
        for i in range(2, limit):
            square = i * i
            count -= n // square
        
        return count
    
    return count_square_free(r) - count_square_free(l - 1)

def find_last_square_free(lPlusOne, rightEnd):
    last_square_free = None

    # 제곱ㄴㄴ수의 개수 계산
    square_free_count = count_square_free_in_range(lPlusOne, rightEnd)

    # 마지막 제곱ㄴㄴ수 찾기
    for n in range(rightEnd, lPlusOne - 1, -1):
        if is_square_free(n):
            last_square_free = n
            break
    
    return last_square_free

def is_square_free(n):
    # n이 제곱수로 나누어지지 않는지 확인
    limit = int(math.sqrt(n)) + 1
    
    for i in range(2, limit):
        if n % (i * i) == 0:
            return False
    
    return True
