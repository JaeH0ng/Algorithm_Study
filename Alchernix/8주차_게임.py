#36ms
X, Y = map(int, input().split())
Z = int(Y * 100 / X)

def binary_search(target, X_start, X_end, X_original, Y_original):
    while X_start <= X_end:
        X_mid = (X_start + X_end) // 2
        Y_mid = Y_original + (X_mid - X_original)
        rate = int(Y_mid * 100 / X_mid)
        if rate >= target and int((Y_mid - 1) * 100 / (X_mid - 1)) < target:
            return X_mid - X_original #이겨야하는 최소 횟수
        elif rate >= target:
            X_end = X_mid - 1
        else:
            X_start = X_mid + 1
    return -1

result = binary_search(Z + 1, X, 2 * X, X, Y)
print(result)
