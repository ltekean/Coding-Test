def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    my_list=[]
    
    for i in score:
        my_list.append(i)
        if len(my_list) == m:
            answer+=m*my_list[-1]
            my_list=[]
    return answer

# def solution(k, m, score):
#     answer = 0

#     score.sort()
#     while len(score) >= m:
#         for _ in range(m - 1):
#             score.pop()
#         if score:
#             answer += min(score.pop(), k) * m
#         else:
#             break

#     return answer