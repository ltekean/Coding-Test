N = int(input())
num = 0
M = N
while True:
    A = N // 10
    B = N % 10
    N = 10*B + (A+B)%10
    num += 1
    if N == M:
        break
print(num)