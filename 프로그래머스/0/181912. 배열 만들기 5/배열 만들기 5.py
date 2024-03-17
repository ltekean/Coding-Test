def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        aa = i[s:s+l]
        if int(aa) > k:
            answer.append(int(aa))
    return answer