def solution(sizes):
    answer = 0
    garo = 0
    sero = 0
    for size in sizes:
        size.sort()
        if size[0] > garo:
            garo = size[0]
        if size[1] > sero:
            sero = size[1]
    return garo*sero