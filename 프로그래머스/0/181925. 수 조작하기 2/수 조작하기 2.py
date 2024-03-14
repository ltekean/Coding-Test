def solution(numLog):
    result = []
    current_num = 0  # 초기값은 0으로 설정
    for i in range(len(numLog)):
        diff = numLog[i] - current_num
        if diff == 1:  # 1을 더한 경우
            result.append("w")
        elif diff == -1:  # 1을 뺀 경우
            result.append("s")
        elif diff == 10:  # 10을 더한 경우
            result.append("d")
        elif diff == -10:  # 10을 뺀 경우
            result.append("a")
        current_num = numLog[i]  # 현재 수를 업데이트
    return ''.join(result)