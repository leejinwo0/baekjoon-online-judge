import sys
input = sys.stdin.readline

room = int(input())
count = 1
result = 1

while room > 1:
    room -= 6 * count
    result += 1
    count +=1

print(result)