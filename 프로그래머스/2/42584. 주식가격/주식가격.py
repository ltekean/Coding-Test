def solution(prices):
    n = len(prices)
    result = [0] * n  # 결과를 저장할 리스트 초기화
    stack = []  # 가격이 떨어지지 않은 기간을 추적하기 위한 스택

    for i in range(n):
        # 스택이 비어있지 않고, 가격이 떨어졌을 때
        while stack and prices[stack[-1]] > prices[i]:
            # 스택에서 빼내어 해당 기간 동안 가격이 떨어지지 않음을 업데이트
            j = stack.pop()
            result[j] = i - j
        
        # 현재 인덱스를 스택에 추가
        stack.append(i)
    
    # 마지막까지 가격이 떨어지지 않은 기간을 처리
    while stack:
        j = stack.pop()
        result[j] = n - 1 - j
    
    return result