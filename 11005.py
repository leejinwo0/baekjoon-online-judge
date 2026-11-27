import sys
input = sys.stdin.readline

N, B = map(int, input().split())
result=[]

while True:
    if N > 0:
        remainder = N % B

        if remainder < 10:
            result.append(chr(remainder + ord('0')))
        else:
            result.append(chr(remainder - 10 + ord('A')))

        N //= B
    else:
        break

print("".join(result[::-1]))