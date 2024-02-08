def solution(price):
    if price < 100000:
        return price
    elif 100000<= price < 300000:
        return price*95//100
    elif 300000<= price < 500000:
        return price*9//10
    else:
        return price*8//10