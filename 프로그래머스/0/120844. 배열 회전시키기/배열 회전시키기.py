def solution(numbers, direction):
    answer = []
    if direction == "right":
        a = numbers[-1]
        numbers.pop(-1)
        numbers.insert(0,a)
    else:
        b = numbers[0]
        numbers.pop(0)
        numbers.append(b)
    return numbers