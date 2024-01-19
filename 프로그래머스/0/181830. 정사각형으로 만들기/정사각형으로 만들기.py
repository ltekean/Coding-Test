def solution(arr):
    # 이차원 배열의 행과 열의 수 구하기
    num_rows = len(arr)
    num_cols = len(arr[0]) if num_rows > 0 else 0

    # 행의 수가 더 많으면 열의 수를 맞춰주기
    if num_rows > num_cols:
        for row in arr:
            while len(row) < num_rows:
                row.append(0)
    
    # 열의 수가 더 많으면 행의 수를 맞춰주기
    elif num_cols > num_rows:
        while len(arr) < num_cols:
            arr.append([0] * num_cols)

    return arr
