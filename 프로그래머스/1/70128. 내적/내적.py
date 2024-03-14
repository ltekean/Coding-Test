def solution(a, b):
    # 내적을 저장할 변수
    dot_product = 0
    
    # 두 배열의 대응하는 원소들을 곱하여 내적에 더함
    for i in range(len(a)):
        dot_product += a[i] * b[i]
    
    return dot_product