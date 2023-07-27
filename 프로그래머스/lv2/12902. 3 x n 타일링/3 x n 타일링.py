def solution(n):
    if n % 2 == 1:
        return 0

    cache = [0] * (n + 1)
    cache[2] = 3
    total_sum = 0

    for i in range(4, n + 1, 2):
        cache[i] = (cache[i - 2] * 3 + (total_sum * 2 + 2)) % 1000000007
        total_sum += cache[i - 2] % 1000000007

    return cache[n]