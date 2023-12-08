def solution(board, moves):
    answer = 0
    doll_list = []

    for move in moves:
        for row in board:
            doll = row[move - 1]
            if doll:
                if doll_list and doll_list[-1] == doll:
                    doll_list.pop()
                    answer += 2
                else:
                    doll_list.append(doll)
                row[move - 1] = 0
                break

    return answer
