import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))[:N]

X = int(input())
count = numbers.count(X)
print(count)