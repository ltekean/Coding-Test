def solution(my_string, indices):
    tmp = list(my_string)  # 문자열을 리스트로 변환하여 쉽게 접근할 수 있도록 함

    # indices를 돌면서 해당 인덱스의 값을 비움
    for index in indices:
        tmp[index] = ''

    # 빈 값들을 제외하고 문자열로 다시 합침
    answer = ''.join(tmp)
    return answer
