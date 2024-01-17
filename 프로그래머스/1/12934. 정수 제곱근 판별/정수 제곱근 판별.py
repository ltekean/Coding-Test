import math

def solution(n):
    a = math.sqrt(n)
    if a.is_integer() == True:
        return (a+1)**2
    return -1