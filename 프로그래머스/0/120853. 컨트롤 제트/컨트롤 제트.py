def solution(s):
    s_list = list(map(str, s.split())) 
    for idx, val in enumerate(s_list):
        if val == "Z":
            s_list[idx-1] = 0  
    s_list = [int(i) for i in s_list if i != "Z"]
    return sum(s_list)

