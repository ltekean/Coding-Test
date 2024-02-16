def solution(start, end_num):
    return sorted([i for i in range(end_num, start+1)], reverse=True)