import sys
input =sys.stdin.readline

remainders = set()

for i in range(10):
    number = int(input())
    remainders.add(number % 42)

print(len(remainders))