# 옷이 a, b 2종류일 때 (1+a)(1+b) - 1 대입
from functools import reduce

def solution(clothes):
    answer = 0
    total = {}
    
    for i in range(len(clothes)):
        total[clothes[i][1]] = total.get(clothes[i][1], 1) + 1
    
    test = total.values()
    answer = reduce(lambda a, b: a * b, test, 1) - 1
    return answer
