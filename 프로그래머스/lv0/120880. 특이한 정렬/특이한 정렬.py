def solution(numlist, n):
    answer =[] # n과의 거리를 저장할 리스트
    for i in numlist:
        answer.append(i - n)
    
    result = [] # 정렬한 배열
    # 거리가 n에 가까운 순으로 정렬, 절댓값이 같으면 양수(= 큰 값) 먼저
    for i in sorted(answer[:], key=lambda x:[abs(x), -x]): 
        result.append(numlist[answer.index(i)])

    return result