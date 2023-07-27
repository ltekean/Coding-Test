def solution(s):
    x = ''
    first_count = 0
    next_count = 0
    result = 0

    for letter in s:
        if x == '':
            x = letter
            first_count += 1
            continue

        if letter == x:
            first_count += 1
        else:
            next_count += 1

        if first_count == next_count:
            result += 1
            first_count = 0
            next_count = 0
            x = ''

    if x:
        result += 1

    return result