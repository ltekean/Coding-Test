def solution(arr):
    cnt = 0
    dx = 10**9
    for idx, i in enumerate(arr):
        if i < dx:
            dx = i
            cnt = idx
    arr.pop(cnt)
    if not arr:
        return [-1]
    return arr
