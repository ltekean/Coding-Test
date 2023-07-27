# 각 지표마다 서로 비교를 통해 더 큰 값을 return 값에 넣는 것
# >> 비교계산 식을 만들어줘야 함
# 비교의 대상끼리만 비교해야 하기 때문에 RT, CF, JM, AN으로 묶어놓음
# return data type : str

def solution(survey, choices):
    answer = ''
    dic = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    # RT, CF, JM, AN으로 묶을 것을 염두
    
    for surv, choi in zip(survey, choices):
        if choi>4: dic[surv[1]] += choi-4
        elif choi<4: dic[surv[0]] += 4-choi
    #유형의 survey들을 모두 계산
    
    
    # list로 refactoring 해보고 싶어서 바꿔봄
    res = list(dic.items())
    # 딕셔너리 dic의 key-value 쌍을 튜플로 반환, 한 것을 리스트화
    # [("R", 3), ("T", 5), ("C", 2), ("F", 4), ("J", 1), ("M", 6), ("A", 0), ("N", 2)]
    
    for i in range(0,8,2): # 묶은 것끼리 비교
        if res[i][1] >= res[i+1][1]:
            answer += res[i][0]
        else:
            answer += res[i+1][0]
    # 조사를 계산한 것을 토대로 더 큰 숫자의 유형을 뽑는 함수
        
    return str(answer)