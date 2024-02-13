def solution(n):
    a = 1
    for i in range(1,10000):
        if a>n:
            return i-2
        a *= i