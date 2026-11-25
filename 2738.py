import sys
input = sys.stdin.readline

N, M = map(int, input().split())

row_N = [[0] * M for n in range(N)]
row_M = [[0] * M for n in range(N)]

for n in range(N):
    row = list(map(int, input().split()))
    row_N[n] = row

for n in range(N):
    row = list(map(int, input().split()))
    row_M[n] = row

for i in range(N):
    for j in range(M):
        print(row_N[i][j] + row_M[i][j], end=" ")
    print()