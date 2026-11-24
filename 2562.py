import sys
input = sys.stdin.readline

numbers = []

while True:
    try:
        numbers.append(int(input()))
    except:
        break

max_number = max(numbers)
print(max_number)
print(numbers.index(max_number) + 1)