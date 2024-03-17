def solution(arr, intervals):
    answer = []
    for inter in intervals:
        for i in range(inter[0], inter[1]+1):
            answer.append(arr[i])
    return answer