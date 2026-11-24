import sys
input = sys.stdin.readline

N, M = map(int, input().split())
baskets = []

for a in range(N):
    baskets.append(a + 1)

for b in range(M):
    i, j = map(int, input().split())
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

print(*baskets)