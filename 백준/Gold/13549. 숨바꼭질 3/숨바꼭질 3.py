from collections import deque

def hide_and_seek(N, K):
    # 수빈이와 동생의 위치를 표현하는 리스트
    positions = [-1] * 100001

    # 초기 위치 설정
    start = N
    target = K
    positions[start] = 0

    # BFS를 위한 큐 초기화
    queue = deque()
    queue.append(start)

    while queue:
        current = queue.popleft()

        # 현재 위치를 기준으로 다음 위치 계산
        teleport = current * 2  # 순간이동
        move_left = current - 1
        move_right = current + 1

        # 순간이동은 0초에 도착하므로 먼저 처리
        if teleport <= 100000 and positions[teleport] == -1:
            positions[teleport] = positions[current]
            queue.append(teleport)

        # 좌우로 이동하는 경우
        for move in (move_left, move_right):
            if 0 <= move <= 100000 and positions[move] == -1:
                positions[move] = positions[current] + 1
                queue.append(move)

        # 목표 도달 시 종료
        if positions[target] != -1:
            break

    return positions[target]

def main():
    N, K = map(int, input().split())
    result = hide_and_seek(N, K)
    print(result)

if __name__ == "__main__":
    main()
