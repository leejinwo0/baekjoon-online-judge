import sys
input = sys.stdin.readline

star = int(input())

for i in range(star):
    print(' ' * (star - i - 1) + '*' * (2 * i + 1))
for j in range(star - 1):
    print(' ' * (j + 1) + '*' * (2 * (star - j - 1) - 1))