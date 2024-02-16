def solution(myString, pat):
    answer = ""
    for i in myString:
        if i =="A":
            answer += "B"
        else:
            answer += "A"
    return int(pat in answer)
