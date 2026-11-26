import sys
input = sys.stdin.readline

word = input().rstrip()
word = word.upper()
count = {}
for char in word:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

max_count = max(count.values())
max_chars = [char for char, count in count.items() if count == max_count]

if len(max_chars) == 1:
    print(max_chars[0])
else:
    print("?")