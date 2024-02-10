def solution(arr):
    cnt = 0
    while True:
        modified = False  # 변경 여부를 나타내는 플래그 변수
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] /= 2
                modified = True  # 배열이 변경되었음을 표시
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
                modified = True  # 배열이 변경되었음을 표시
        if not modified:  # 배열이 변경되지 않았다면 루프 종료
            break
        else:
            modified =False
            cnt += 1
            continue
    return cnt
