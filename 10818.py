import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))[:N]

print(min(numbers), max(numbers))