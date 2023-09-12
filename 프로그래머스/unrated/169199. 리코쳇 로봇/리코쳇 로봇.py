import collections

def find_next(x,y,tx,ty, board):
    while True:
        nx, ny = x, y

        x += tx
        y += ty

        if not 0<=x<len(board) or not 0<=y<len(board[0]) or board[x][y] == 'D':
            return nx, ny    

def solution(board):
    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                rx, ry = i,j
            if board[i][j] == 'G':
                gx, gy = i,j     

    move = {(-1,0), (0,1), (1,0), (0,-1)}

    q = collections.deque()
    q.append((rx,ry,0))
    visited[rx][ry] = 1

    while q:
        x,y,cnt = q.popleft()

        if x == gx and y == gy:
            return cnt

        for tx,ty in move:
            nx, ny = find_next(x,y,tx,ty,board)

            if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] != 'D' and visited[nx][ny] == 0:
                q.append((nx,ny,cnt+1))
                visited[nx][ny] = 1

    return -1