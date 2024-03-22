from collections import deque

def solution(arr):
    stk = deque()
    i = 0
    
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        else:
            stk.pop()
    
    return list(stk)
