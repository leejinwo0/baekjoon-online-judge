import sys
input = sys.stdin.readline

N = int(input())
numbers = input().rstrip()

sum = 0

for i in range(len(numbers)):
    sum += int(numbers[i])

print(sum)