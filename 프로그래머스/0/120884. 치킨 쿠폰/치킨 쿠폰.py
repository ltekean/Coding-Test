def solution(chicken):
    total_chicken = chicken  # 주문한 치킨 수
    coupons = 0  # 현재 보유한 쿠폰 수
    free_chicken = 0  # 받은 서비스 치킨 수

    while total_chicken > 0:
        # 주문한 치킨으로 쿠폰 발급
        coupons += total_chicken
        total_chicken = 0

        # 쿠폰으로 서비스 치킨 받기
        free_chicken += coupons // 10
        total_chicken += coupons // 10  # 서비스 치킨으로 받은 치킨 수를 다시 주문에 추가
        coupons %= 10  # 남은 쿠폰 수

    return free_chicken