def solution(my_string, is_prefix):
    a = len(is_prefix)
    return int(my_string[:a] == is_prefix)