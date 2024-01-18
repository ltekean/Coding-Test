def solution(seoul):
    count = 0
    for i in seoul:
        if i != "Kim":
            count += 1
        else:
            return f"김서방은 {count}에 있다"