def solution(arr, queries):
    answer = []
    for query in queries:
        for i in range(query[0], query[1]+1):
            if i < len(arr):
                arr[i] += 1
    return arr