def solution(str1, str2):
    answer = ''
    for i in zip(str1, str2):
        answer += ''.join(i)
    return answer
