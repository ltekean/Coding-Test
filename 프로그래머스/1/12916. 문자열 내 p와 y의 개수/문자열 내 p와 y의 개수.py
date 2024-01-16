def solution(s):
    pcount, ycount = 0,0
    case = s.lower()
    for i in case:
        if i == "p":
            pcount += 1
        elif i == "y":
            ycount += 1
    if pcount == ycount:
        return True
    else:
        return False