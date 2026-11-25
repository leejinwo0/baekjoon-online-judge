import sys
input = sys.stdin.readline

N = int(input())

for i in range(0, N):
    R, S = input().split()
    R = int(R)
    for j in range(0, len(S)):
        print(S[j] * R, end='')
    print()