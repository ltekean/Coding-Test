def my_dict(iterables, repeat):
    if repeat == 0:
        yield ()
        return
    for item in iterables:
        for rest in my_dict(iterables, repeat - 1):
            yield (item,) + rest

def solution(word):
    answer = 0
    
    result = list()
    for i in range(1, 6):
        li = list(my_dict(["A", "E", "I", "O", "U"], i))
        for j in li:
            result.append(''.join(j))
        
    result.sort()
    answer = result.index(word) + 1

    return answer