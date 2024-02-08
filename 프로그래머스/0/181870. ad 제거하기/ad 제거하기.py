def solution(strArr):
    result = []
    for i in strArr:
        if not "ad" in i:
            result.append(i)
    return result