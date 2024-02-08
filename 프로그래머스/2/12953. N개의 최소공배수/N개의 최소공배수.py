def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(arr):
    a= 1
    for ar in arr:
        b = a * ar // gcd(a, ar)
        a = b
    return a