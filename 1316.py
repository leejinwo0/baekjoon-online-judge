import sys
input = sys.stdin.readline

count = 0
N = int(input())

for i in range(N):
    word = input().rstrip()
    if list(word) == sorted(word, key=word.find):
        count += 1

print(count)
    