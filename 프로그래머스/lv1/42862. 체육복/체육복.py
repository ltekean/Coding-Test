# 바로 앞뒤번호에게만 체육복 빌려주기 가능
# 전체 학생 수 n, 도난당한 학생 번호 배열 lost, 여벌 체육복 배열 reserve
# lost에서 단어 하나만 빼오고 reserve에 그 앞뒤번호가 있는지 확인
# 있으면 빌려주고, 없으면 n -= 1하고 pass

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for i in lost[:]:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    for a in lost[:]:
        if a-1 in reserve:
            lost.remove(a)
            reserve.remove(a-1)
        elif a+1 in reserve:
            lost.remove(a)
            reserve.remove(a+1)

    return n - len(lost)