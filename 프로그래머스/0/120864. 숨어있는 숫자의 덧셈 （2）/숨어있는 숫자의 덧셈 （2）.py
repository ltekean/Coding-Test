def solution(my_string):
    numbers = ''.join(char if char.isdigit() else ' ' for char in my_string).split()  # 문자열에서 자연수를 추출합니다.
    total_sum = sum(int(num) for num in numbers)  # 추출한 자연수들의 합을 계산합니다.
    return total_sum