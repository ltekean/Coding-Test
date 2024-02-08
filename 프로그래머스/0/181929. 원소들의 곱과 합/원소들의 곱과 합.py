def solution(num_list):
    product = 1
    sum_of_elements = sum(num_list)
    
    for num in num_list:
        product *= num
    
    return int(product < sum_of_elements ** 2)