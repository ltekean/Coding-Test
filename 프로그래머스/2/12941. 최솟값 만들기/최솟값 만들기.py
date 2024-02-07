def solution(A,B):
    answer = 0
    p = 0
    A.sort()
    B.sort(reverse=True)
    for q,w in zip(A,B):
        answer += q*w
    return answer