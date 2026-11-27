import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    result = []
    C = int(input())

    for i in range(4):
        if i == 0:
            result.append((C // 25))
            C = C - 25 * (C // 25)
        elif i == 1:
            result.append((C // 10))
            C = C - 10 * (C // 10)
        elif i == 2:
            result.append((C // 5))
            C = C - 5 * (C // 5)
        else:
            result.append((C // 1))

    print(*result)