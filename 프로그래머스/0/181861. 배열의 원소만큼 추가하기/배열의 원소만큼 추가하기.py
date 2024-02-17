def solution(arr):
    answer = []
    
    for i in arr:
        cnt = 0
        while cnt<i:
            answer.append(i)
            cnt+=1
    return answer