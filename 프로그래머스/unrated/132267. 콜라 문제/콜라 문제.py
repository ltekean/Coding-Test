# a / b = 비율
# n // (a/b)
# a = 5 b = 2 n = 20
# 20 //(5/2)

def solution(a, b, n):
    answer = 0
    while (n >= a):
        storage = n % a
        n = (n//a) * b
        answer += n
        n += storage
    return answer