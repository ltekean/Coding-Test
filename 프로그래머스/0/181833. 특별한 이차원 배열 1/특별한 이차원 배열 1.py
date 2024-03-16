def solution(n):
    answer = []
    for i in range(n):
        lis = [0]*n
        lis[i] = 1
        answer.append(lis)
    return answer