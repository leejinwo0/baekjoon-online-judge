A, B = map(int, input().split())
C = int(input())

total = A * 60 + B + C
A = total // 60
B = total % 60
if A >= 24:
    A = A - 24

print(A, B)