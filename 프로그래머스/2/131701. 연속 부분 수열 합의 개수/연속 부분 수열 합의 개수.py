def solution(elements):
    
    l = len(elements)
    sum_set = set() # set()을 통해 중복 방지
    
    # 원소 하나를 기준으로 차례대로 더한 후
    # 더할 때 마다 set()에 추가
    for i in range(l):
        v = elements[i]
        sum_set.add(v)
        
        for j in range(i+1, i+l):
            v += elements[j%l]
            sum_set.add(v)
    
    return len(sum_set)