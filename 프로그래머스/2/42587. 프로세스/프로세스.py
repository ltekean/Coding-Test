def solution(priorities, location):
    cnt = 0
    while True:
        # 첫 번째 문제 항목이 최대 우선 순위인지 확인
        if priorities[0] == max(priorities):
            cnt += 1
            # 문제를 해결한 경우
            if location == 0:
                return cnt
            else:
                # 문제를 해결하지 않았지만 우선 순위가 가장 높은 경우
                priorities.pop(0)
                location -= 1
        else:
            # 우선 순위가 가장 높지 않은 경우, 맨 앞의 문제를 맨 뒤로 이동
            priorities.append(priorities.pop(0))
            # location 조정
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1