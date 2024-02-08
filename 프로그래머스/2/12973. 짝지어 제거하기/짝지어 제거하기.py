def solution(s):
    stack = []  # 문자를 저장할 스택

    for char in s:
        # 스택이 비어있지 않고, 스택의 마지막 문자가 현재 문자와 같다면 짝이 만들어짐
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    # 스택이 비어있다면 모든 짝을 제거할 수 있음
    return 1 if not stack else 0