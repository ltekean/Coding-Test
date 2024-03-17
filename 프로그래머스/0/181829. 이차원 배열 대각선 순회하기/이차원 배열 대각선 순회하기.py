def solution(board, k):
    answer = 0
    n_rows = len(board)
    n_cols = len(board[0]) if board else 0  # Assuming at least one row exists
    for i in range(n_rows):
        for j in range(n_cols):
            if i + j <= k:
                answer += board[i][j]
    return answer
