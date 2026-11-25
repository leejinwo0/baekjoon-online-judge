import sys
input = sys.stdin.readline

word = input().rstrip()
sum = 0

for i in range(len(word)):
    if word[i] == "1":
        sum += 2
    elif word[i] in "ABC":
        sum += 3
    elif word[i] in "DEF":
        sum += 4
    elif word[i] in "GHI":
        sum += 5
    elif word[i] in "JKL":
        sum += 6
    elif word[i] in "MNO":
        sum += 7
    elif word[i] in "PQRS":
        sum += 8
    elif word[i] in "TUV":
        sum += 9
    elif word[i] in "WXYZ":
        sum += 10
    else:
        sum += 11
print(sum)
