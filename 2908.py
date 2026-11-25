import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())

A = int(''.join(reversed(str(A))))
B = int(''.join(reversed(str(B))))

if A > B:
    print(A)
else:
    print(B)