import sys
input = sys.stdin.readline

paper = [[0] * 100 for i in range(100)]

num = int(input())
for n in range(num):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

total = sum(sum(row) for row in paper)
print(total)