def solution(num_list):
    odd, even = 0,0
    for idx, i in enumerate(num_list):
        if idx%2==0:
            even += i
        else:
            odd += i
    return max(even,odd)