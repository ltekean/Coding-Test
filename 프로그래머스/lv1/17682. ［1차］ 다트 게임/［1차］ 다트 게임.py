# def solution(dartResult):
#     dicx = ['S','D','T']
#     answer = []
#     dartResult = dartResult.replace('10','x')
#     for i in range(len(dartResult)):
#         if dartResult[i] in dic:
#             if dartResult[i-1] == 'x':
#                 answer.append(pow(10, dic.index(dartResult[i])+1))
#             else:
#                 answer.append(pow(int(dartResult[i-1]), dic.index(dartResult[i])+1))
#     for i in range(len(dartResult)):
#         num = i//2
#         if num == 1:
#             if dartResult[i] == '*':
#                 answer[0] *= 2 
#             elif dartResult[i] == '#':
#                 answer[0] *=  - 1 
#         elif num == 2:
#             if dartResult[i] == '*':
#                 answer[0] *= 2
#                 answer[1] *= 2
#             elif dartResult[i] == '#':
#                 answer[1] *=  - 1 
#         elif (num == 3) or (num == 4):   
#             if dartResult[i] == '*':
#                 answer[1] *= 2
#                 answer[2] *= 2
#             elif dartResult[i] == '#':
#                 answer[2] *=  - 1 
#     return sum(answer)

def solution(dartResult):
    answer = []
    dartResult = dartResult.replace('10', 'x')
    dic = { 'S':1, 'D':2, 'T':3 }
    
    for n in dartResult:
        if n in dic:
            answer[-1] = answer[-1]**dic[n]
        elif n == '#':
            answer[-1] *= -1
        elif n == '*':
            answer[-1] *= 2
            if len(answer) > 1:
                answer [-2] *= 2
        elif n == 'x':
            answer.append(10)
        else:
            answer.append(int(n))

    return sum(answer)