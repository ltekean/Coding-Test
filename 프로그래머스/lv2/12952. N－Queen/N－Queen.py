def nqueen(queens, next_queen, n):
    global answer

    if next_queen in queens:  # 같은 행에 있는지 체크
        return

    for row, col in enumerate(queens):
        next_queen_row = len(queens)
        if abs(next_queen - col) == next_queen_row - row:  # 대각선에 있는지 체크
            return

    queens.append(next_queen)

    if len(queens) == n:
        answer += 1
        return

    for next_queen in range(n):
        nqueen(queens[:], next_queen, n)


def solution(n):
    global answer
    answer = 0

    for next_queen in range(n):
        queens = []
        nqueen(queens, next_queen, n)

    return answer

# ans = 0
# chkX = [False for i in range(32)]
# chkCross1 = [False for i in range(32)]
# chkCross2 = [False for i in range(32)]

# def nq(y, n):
#     global ans
#     x = 0
#     if y > n:
#         ans+=1
#     for x in range(1, n+1):
#         if chkX[x] or chkCross1[y + x] or chkCross2[(y - x) + n]:
#             continue
#         chkX[x] = True
#         chkCross1[y + x] = True
#         chkCross2[(y - x) + n] = True

#         nq(y + 1, n)
#         chkX[x] = False
#         chkCross1[y + x] = False
#         chkCross2[(y - x) + n] = False

# def solution(n):
#     nq(1, n)
#     return ans