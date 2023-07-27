# def solution(nums):
#     answer = 0
#     dict={}
#     for n in nums:
#         dict[n] = 1
#         # 중복된 n이 있다면 딕셔너리의 값이 계속 1로 유지됨.(hash(value)를 통한 거르기)
#         # nums 리스트의 각 원소들이 중복되지 않고 저장됨(set으로 해도 되겠는데?)
#     if len(nums) // 2 <= len(dict):
#         return len(nums) // 2
#     return len(dict)

def solution(nums):

    # if len(nums) // 2 > num_set:
    #     return num_set
    # else:
    #     return len(nums) // 2
    return min(len(set(nums)), len(nums)//2)