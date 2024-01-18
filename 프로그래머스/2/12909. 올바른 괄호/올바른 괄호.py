def solution(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False  # 닫는 괄호가 왔는데 열린 괄호가 없는 경우
            stack.pop()

    return not stack  # 스택이 비어있으면 올바른 괄호, 비어있지 않으면 올바르지 않은 괄호