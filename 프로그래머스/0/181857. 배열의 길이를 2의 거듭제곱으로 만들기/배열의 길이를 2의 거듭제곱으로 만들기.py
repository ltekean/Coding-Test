def solution(arr):
    answer = []
    cnt = 1
    while len(arr) > cnt:
        cnt *= 2
    while len(arr) < cnt:
        if len(arr) < cnt:
            arr.append(0)
    return arr