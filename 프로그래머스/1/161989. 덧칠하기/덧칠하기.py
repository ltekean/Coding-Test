def solution(n, m, section):
    answer = 1
    paint = section[0] # 덧칠 시작점
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]
            
    return answer

# n = 페인트 칠해진 길이
# m = 롤러의 길이
# section = 페인트를 다시 칠해야 하는 구역 번호 배열