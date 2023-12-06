def solution(data, ext, val_ext, sort_by):
    answer = []
    dict = {"code":0, "date":1, "maximum":2, "remain":3}
    for d in data:
        value = d[dict[ext]]
        # 딕셔너리에서 dict[ext]는 ext의 값(value)를 뜻함; 리스트와 다름.
        if value <= val_ext:
            answer.append(d)
    answer.sort(key = lambda x : x[dict[sort_by]])
    return answer