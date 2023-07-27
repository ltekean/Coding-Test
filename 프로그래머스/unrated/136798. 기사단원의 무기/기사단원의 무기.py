def cd(n): # 약수 출력
    list_ = []
    for i in range(1,int(n**0.5)+1): # 범위 설정(제곱근까지만 구해서 복잡도 감소)
        if n%i == 0: # 약수 조건이 될 시
            list_.append(n//i) 
            list_.append(i) # 약수들을 a 리스트에 첨부
    return len(set(list_)) # 중복되는 수를 제거한 후 길이 반환
def solution(number, limit, power):
    total = 0
    for a in range(1, number+1):
        if cd(a) <= limit:
            total += cd(a)
        else:
            total += power
    return total