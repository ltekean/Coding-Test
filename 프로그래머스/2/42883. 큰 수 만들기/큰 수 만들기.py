def solution(number, k):
    # 스택 선언
    stack = []
    
    # number의 길이만큼 for loop
    for num in number:
        # 1. 제거할 수 k가 남았고
        # 2. 스택에 값이 있고
        # 3. 스택의 마지막 값이 num보다 작다면
        # 제거 후 제거할 수 k를 1씩 감소 
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        # 스택에 num 추가
        stack.append(num)
    
    # k가 남아있는 경우 - 테스트 케이스 number: "93939", k: 2, 출력: 999, 실제정답: 99
    if k != 0:
        stack = stack[:-k]
    
    # 배열을 문자열로 바꿔주고 반환
    return ''.join(stack)