import sys
input = sys.stdin.readline

words = [input().strip() for i in range(5)]

for j in range(15):
    for word in words:
        if j < len(word):
            print(word[j], end='')