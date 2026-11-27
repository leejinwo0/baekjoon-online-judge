import sys
input = sys.stdin.readline

X = int(input())

if X == 1:
    print("1/1")
else:
    line = 1
    while X > line:
        X -= line
        line += 1
    if line % 2 == 0:
        A = X
        B = line - X + 1
    else:
        A = line - X + 1
        B = X

    print(str(A) + "/" + str(B))