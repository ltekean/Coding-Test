def solution(array):
    a = len(array)
    array.sort()
    return array.pop(a//2)