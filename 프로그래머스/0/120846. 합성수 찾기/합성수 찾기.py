def solution(n):
    composite_count = 0  # 합성수의 개수를 저장할 변수
    
    # 2부터 n까지 각 수마다 약수의 개수를 세어 합성수인지 판별합니다.
    for num in range(2, n+1):
        divisor_count = 0  # 약수의 개수를 저장할 변수
        # 1부터 num까지 각 수마다 num이 그 수의 약수인지 확인합니다.
        for i in range(1, num+1):
            if num % i == 0:  # num을 i로 나누어 떨어지는지 확인합니다.
                divisor_count += 1  # 나누어 떨어진다면 약수의 개수를 증가시킵니다.
        
        # 약수의 개수가 세 개 이상인 경우 합성수로 간주하고 합성수의 개수를 증가시킵니다.
        if divisor_count >= 3:
            composite_count += 1
    
    return composite_count
