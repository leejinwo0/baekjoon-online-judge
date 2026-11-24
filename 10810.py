import sys
input = sys.stdin.readline

N, M = map(int, input().split())
baskets = [0] * N
for basket in range(0, M):
    i, j, k = map(int, input().split())
    for ball in range(i, j + 1):
        baskets[ball - 1] = k
print(*baskets)