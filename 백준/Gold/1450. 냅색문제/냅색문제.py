# 세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.

# N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성하시오.

# 예시를 보니 물건을 아예 넣지 않는 경우도 있다고 판단
# 적당히 순열 조합을 사용하면 사실 완전탐색으로 해결이 가능하지만..
from sys import stdin
input = stdin.readline

import sys

def dfs(s, e, _sum, v):
    if s >= e:
        v.append(_sum)
        return
    dfs(s + 1, e, _sum, v)
    dfs(s + 1, e, _sum + arr[s], v)

n, c = map(int, input().split())
arr = list(map(int, input().split()))
lv = []
rv = []

def main():
    dfs(0, n // 2, 0, lv)
    dfs(n // 2, n, 0, rv)
    
    lv.sort()
    ans = 0
    for ele in rv:
        if ele > c:
            continue
        left = 0
        right = len(lv)
        mid = 0
        while left < right:
            mid = (left + right) // 2
            if ele + lv[mid] > c:
                right = mid
            else:
                left = mid + 1
        ans += right
    
    print(ans)

if __name__ == "__main__":
    main()

