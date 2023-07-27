def solution(lottos, win_nums):
    ranklist = [6, 6, 5, 4, 3, 2, 1]
    bigger = ranklist[len(set(lottos) & set(win_nums)) + lottos.count(0)]
    smaller = ranklist[len(set(lottos) & set(win_nums))]
    return [bigger, smaller]
# 대광운
# def solution(lottos, win_nums):
#     bigger = abs(len(set(win_nums) - set(lottos)) + lottos.count(0))
#     smaller = abs(len(set(win_nums) - set(lottos)))
#     return [bigger, smaller]