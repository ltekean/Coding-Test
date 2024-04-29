# def solution(want, number, discount):
#     answer = 0
#     stack = []
#     wanna = [i * number[idx] for idx, i in enumerate(want)]

#     for i in range(len(discount)):
#         stack.append(discount[i])
#         if stack[-10:] in wanna:
#             answer += 1
#     print(stack)
#     return answer

from collections import Counter

def solution(want, number, discount):
    answer = 0
    dict = {}
    for i, j in zip(want, number):
        dict[i] = j
    
    for a in range(len(discount)-9):
        cnt = Counter(discount[a:a+10])
        if cnt == dict:
            answer += 1
    return answer

# 10일 연속으로 discount가 want에 속해야 한다.
# number 숫자의 합은 10
# Zip 함수와 Counter 함수를 쓰면 쉽게 해결은 될 것 같다.