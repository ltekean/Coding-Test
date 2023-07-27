# 총 366일
# idx(날짜 % 7) : 요일
# 

def solution(a, b):
    dayday = ('FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU')
    month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    answer = sum(month[:a-1]) +b - 1 
    return dayday[answer%7]


solution = lambda a, b: ("FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU")[(sum([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:a - 1]) + b - 1) % 7]
# 1월 : 31일
# 2월 : 29일
# 3월 : 31일
# 4월 : 30일
# 5월 : 31일
# 6월 : 30일
# 7월 : 31일
# 8월 : 31일
# 9월 : 30일
# 10월 : 31일
# 11월 : 30일
# 12월 : 31일