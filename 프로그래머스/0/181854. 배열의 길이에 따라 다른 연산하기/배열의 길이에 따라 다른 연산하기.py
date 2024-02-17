def solution(arr, n):
    answer = []
    a = len(arr)
    if a%2==1:
        for i in range(0, a, 2):
            arr[i] += n
    else:
        for i in range(1, a, 2):
            arr[i] += n
    return arr