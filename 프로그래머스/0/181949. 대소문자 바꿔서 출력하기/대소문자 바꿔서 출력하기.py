str = input()
result_str = ""
for char in str:
    if char.isupper():
        result_str += char.lower()
    elif char.islower():
        result_str += char.upper()
    else:
        result_str += char  # 알파벳이 아닌 문자는 그대로 유지
print(result_str)