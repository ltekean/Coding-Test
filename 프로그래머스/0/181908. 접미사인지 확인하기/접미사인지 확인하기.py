def solution(my_string, is_suffix):
    a = len(is_suffix)
    return int(my_string[-a:] == is_suffix)