import sys
input = sys.stdin.readline

N, M = map(int, input().split())
baskets =[]

for a in range(N):
    baskets.append(a + 1)

for _ in range(M):
    i, j = map(int, input().split())
    baskets[i-1:j] = reversed(baskets[i-1:j])

print(*baskets)