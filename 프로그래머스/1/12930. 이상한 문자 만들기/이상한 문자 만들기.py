def solution(s):
    words = s.split(' ')  # 공백을 기준으로 문자열을 단어로 나눕니다.
    result = []

    for word in words:
        modified_word = ""
        for i in range(len(word)):
            if i % 2 == 0:  # 짝수번째 알파벳
                modified_word += word[i].upper()
            else:
                modified_word += word[i].lower()
        result.append(modified_word)

    return ' '.join(result)