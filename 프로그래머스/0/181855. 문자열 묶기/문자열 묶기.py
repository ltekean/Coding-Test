def solution(strArr):
    answer = [0] * 30
    result = 0
    for i in strArr:
        a = len(i)
        answer[a-1] += 1
    return max(answer)