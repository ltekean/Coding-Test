def solution(N, number):
    # 최솟값이 8보다 큰 경우 -1을 반환
    INF = 8
    # N을 사용한 횟수를 저장하는 배열
    dp = [set() for _ in range(INF + 1)]

    # 숫자 N을 사용하는 횟수 초기화
    for i in range(1, INF + 1):
        dp[i].add(int(str(N) * i))

    # 사칙연산을 활용하여 number를 만들 수 있는지 확인
    for i in range(1, INF + 1):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)

        # number를 만들었을 때의 횟수가 i와 같다면 해당 횟수 반환
        if number in dp[i]:
            return i

    # 최솟값이 8보다 큰 경우 -1 반환
    return -1