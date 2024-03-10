def solution(N, A, B):
    round_count = 0
    while A != B:
        round_count += 1
        A = (A + 1) // 2
        B = (B + 1) // 2
    return round_count
# n-1, n번끼리 대결
# 다음 라운드에서 다시 1~n/2번을 배정받음
# 게임은 한명이 남을 때까지 진행
#a,b는 언제 만나는가