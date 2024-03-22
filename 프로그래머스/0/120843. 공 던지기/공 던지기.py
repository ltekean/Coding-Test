def solution(numbers, k):
    return numbers[(k*2-2)%len(numbers)]