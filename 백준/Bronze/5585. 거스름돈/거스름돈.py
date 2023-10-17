money = 1000 - int(input())
changes = [500, 100, 50, 10, 5, 1]

cnt = 0
for change in changes:
    if money == 0:
        break
    cnt += money // change
    money = money % change

print(cnt)