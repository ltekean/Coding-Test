def solution(land):
    # 땅의 행의 개수
    n = len(land)
    
    # DP 테이블 초기화
    dp = [[0] * 4 for _ in range(n)]
    
    # 첫 번째 행의 최대값 초기화
    for i in range(4):
        dp[0][i] = land[0][i]
    
    # 다음 행부터 DP 테이블 채우기
    for i in range(1, n):
        for j in range(4):
            # 이전 행에서 현재 열을 제외한 나머지 열 중 최대값을 찾아 현재 위치의 점수와 더함
            max_prev = max(dp[i-1][:j] + dp[i-1][j+1:])
            dp[i][j] = max_prev + land[i][j]
    
    # 마지막 행의 최대값 반환
    return max(dp[n-1])