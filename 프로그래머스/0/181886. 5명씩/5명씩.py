def solution(names):
    result = []
    for i in range(0, len(names), 5):
        group = names[i:i+5]
        result.append(group[0])
    return result
