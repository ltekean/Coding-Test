def solution(n):
    for i in range(n//2):
        if i**2 == n:
            return 1
    return 2