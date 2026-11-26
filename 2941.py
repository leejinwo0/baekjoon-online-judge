import sys
input = sys.stdin.readline

word = input().rstrip()
cro_word = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for cro in cro_word:
    word = word.replace(cro, "*")

print(len(word))