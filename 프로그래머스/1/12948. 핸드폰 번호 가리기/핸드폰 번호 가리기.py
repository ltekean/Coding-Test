import re
def solution(phone_number):
    masked_number = re.sub(r'\d(?=\d{4})', '*', phone_number)
    return masked_number