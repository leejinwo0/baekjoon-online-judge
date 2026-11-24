import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))[:N]
M = max(numbers)
print((sum(numbers) / M * 100)/len(numbers))