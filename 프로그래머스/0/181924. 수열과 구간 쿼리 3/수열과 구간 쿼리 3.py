def solution(arr, queries):
    for i in queries:
        start, end = i[0], i[1]
        arr[start], arr[end] = arr[end], arr[start]
    return arr