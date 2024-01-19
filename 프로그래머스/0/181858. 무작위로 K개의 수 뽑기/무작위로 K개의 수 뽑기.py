# def solution(arr, k):
#     answer = []
#     arr.set()
#     for i in arr:
#         answer.append(i)
#     while len(arr) < k:
#         answer.append(-1)
#     return answer

def solution(arr, k):
    answer = []
    while len(answer) < k:
        for i in arr:
            if i not in answer:
                answer.append(i)
                if len(answer) == k:
                    break
        if len(answer) < k:
            answer.append(-1)
    return answer