def solution(binomial):
    bino = list(binomial.split(" "))
    for idx, i in enumerate(bino):
        if i == "+":
            return int(bino[idx-1]) + int(bino[idx+1])
        elif i == "-":
            return int(bino[idx-1]) - int(bino[idx+1])
        elif i == "*":
            return int(bino[idx-1]) * int(bino[idx+1])
    return int(bino)