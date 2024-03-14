def solution(array):
    count = 0
    for num in array:
        while num > 0:
            if num % 10 == 7:  # 숫자의 일의 자리가 7인지 확인합니다.
                count += 1
            num //= 10  # 숫자를 10으로 나누어 일의 자리를 없앱니다.
    return count