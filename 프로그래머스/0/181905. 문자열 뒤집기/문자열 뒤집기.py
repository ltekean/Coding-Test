def solution(my_string, s, e):
    reversed_substr = my_string[s:e+1][::-1]
    result = my_string[:s] + reversed_substr + my_string[e+1:]
    
    return result