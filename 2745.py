import sys
input = sys.stdin.readline

N, B = input().rstrip().split()
B = int(B)
sum = 0

for i in N:
    if '0' <= i <= '9':
        num = ord(i) - ord('0')
    else:
        num = ord(i) - ord('A') + 10

    sum = sum * B + num

print(sum)