def solution(N, stages):
    answer = []
    a = len(stages)
    for i in range(1, N+1):
        count_i = stages.count(i)
        if a == 0:
            answer.append(0)
        else:
            answer.append(count_i / a)
        a -= count_i
        
    result = sorted(range(len(answer)), key=lambda i: (-answer[i], i))
    return [idx + 1 for idx in result]


# 실패율 : 실패자/스테이지 도달자
# N : 전체 스테이지 수
# stages : 사용자가 있는 스테이지의 번호 담긴 배열
# 실패율이 높은 스테이지부터 내림차순 return