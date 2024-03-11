def solution(prices):
    n = len(prices)
    result = [0] * n 
    stack = []

    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            # 스택에서 빼내어 해당 기간 동안 가격이 떨어지지 않음을 업데이트
            j = stack.pop()
            result[j] = i - j
        
        stack.append(i)
    
    while stack:
        j = stack.pop()
        result[j] = n - 1 - j
    
    return result