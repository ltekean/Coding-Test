from collections import deque

def solution(num_list, n):
    d = deque(num_list)
    d.rotate(-n)
    return list(d)