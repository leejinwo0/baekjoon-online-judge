import sys
input = sys.stdin.readline

N, X = map(int, input().split())
numbers = list(map(int, input().split()))[:N]

for i in range(N):
    if numbers[i] < X:
        print(numbers[i], end=' ')