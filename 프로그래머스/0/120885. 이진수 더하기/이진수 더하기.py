def solution(bin1, bin2):
    sum_decimal = int(bin1, 2) + int(bin2, 2)
    
    # 합을 이진수로 변환하여 반환
    sum_binary = bin(sum_decimal)[2:]
    
    return sum_binary