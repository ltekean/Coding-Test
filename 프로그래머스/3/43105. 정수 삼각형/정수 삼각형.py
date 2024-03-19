# def solution(triangle):
#     answer = 0
#     le = len(triangle)
#     d = [0] * 500
    
#     d[0] = triangle[0][0]
#     d[1] = d[0] + max(triangle[0][0], triangle[0][1])
    
#     for i in range(2, le+1):
#         d[i] = d[i-1] + max(triangle[i][], triangle[i][])
#     return d[le+1]
def solution(triangle):
    # triangle의 높이
    n = len(triangle)
    
    # dp 배열 초기화
    dp = [[0] * i for i in range(1, n + 1)]
    
    # 첫 번째 행의 값은 그대로 입력
    dp[0][0] = triangle[0][0]
    
    # 두 번째 행부터 각 셀의 최댓값을 계산
    for i in range(1, n):
        for j in range(i + 1):
            # 대각선 방향으로 한 칸 오른쪽 이동한 경우
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            # 대각선 방향으로 한 칸 왼쪽 이동한 경우
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            # 대각선 방향으로 이동하지 않은 경우
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    
    # 마지막 행에서 최댓값 반환
    return max(dp[-1])