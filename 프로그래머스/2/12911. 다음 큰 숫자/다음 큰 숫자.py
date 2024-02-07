def cnt(binary_number):
    a = bin(binary_number)[2:]
    count = 0
    for digit in a:
        if digit == '1':
            count += 1
    return count

def solution(n):
    for i in range(n+1, 10**8):
        
        if cnt(i) != cnt(n):
            i += 1
        else:
            return i