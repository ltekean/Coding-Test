def solution(n):
    #n을 3진법으로 변환 → divmod로 만들기
    #변환된 3진법을 뒤집기 → reverse ▶▶▶ += str(y)로 reverse 불필요!
    #3진법을 10진법으로 변환 → 간단히 자릿수별 곱 ▶▶▶ int(k,3)로 바로 10진수 정수로 변환
    #값 반환
    k = ""
    while n > 0:
        n,y=divmod(n, 3)
        k += str(y)
    return int(k, 3)