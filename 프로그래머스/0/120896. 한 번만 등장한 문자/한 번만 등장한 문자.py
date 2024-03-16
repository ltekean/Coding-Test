def solution(s):
    char_count = {}
    
    # 문자열에서 각 문자의 등장 횟수를 카운트
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # 등장 횟수가 1인 문자들을 찾아 리스트에 추가
    unique_chars = []
    for char, count in char_count.items():
        if count == 1:
            unique_chars.append(char)
    
    # 찾은 문자들을 사전 순으로 정렬하여 문자열로 반환
    return ''.join(sorted(unique_chars))