def solution(array):
    answer = []
    arr = sorted(array)
    i = arr[-1]
    answer.append(i)
    answer.append(array.index(i))
    return answer