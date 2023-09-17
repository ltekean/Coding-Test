def solution(num_list):
    answer = []
    a, b = 0, 0
    for i in num_list:
        if i%2 ==0:
            a+=1
        else:
            b+=1
    return [a,b]