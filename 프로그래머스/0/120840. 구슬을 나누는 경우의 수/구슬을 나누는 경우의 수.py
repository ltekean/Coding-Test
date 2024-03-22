import math

def solution(balls, share):
    # 이항 계수를 사용하여 경우의 수 계산
    num_cases = math.comb(balls, share)
    return num_cases