def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def solution(arr):
    a= 1
    for ar in arr:
        b = a * ar // gcd(a, ar)
        a = b
    return a