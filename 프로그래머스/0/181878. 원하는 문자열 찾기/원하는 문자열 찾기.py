def solution(myString, pat):
    pat = pat.lower()
    myString = myString.lower()
    if pat in myString:
        return 1
    return 0