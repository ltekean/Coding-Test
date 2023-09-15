# import collections

# def find_next(x,y,tx,ty, board):
#     while True:
#         nx, ny = x, y

#         x += tx
#         y += ty

#         if not 0<=x<len(board) or not 0<=y<len(board[0]) or board[x][y] == 'D':
#             return nx, ny    

# def solution(board):
#     visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == 'R':
#                 rx, ry = i,j
#             if board[i][j] == 'G':
#                 gx, gy = i,j     

#     move = {(-1,0), (0,1), (1,0), (0,-1)}

#     q = collections.deque()
#     q.append((rx,ry,0))
#     visited[rx][ry] = 1

#     while q:
#         x,y,cnt = q.popleft()

#         if x == gx and y == gy:
#             return cnt

#         for tx,ty in move:
#             nx, ny = find_next(x,y,tx,ty,board)

#             if 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] != 'D' and visited[nx][ny] == 0:
#                 q.append((nx,ny,cnt+1))
#                 visited[nx][ny] = 1

#     return -1

from collections import deque

def bfs(r,c,row,col,data):
    visited = [[float("inf")] * col for i in range(row)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    q.append((r,c))
    visited[r][c] = 0
    while q:
        x,y = q.popleft()
        fx,fy = x,y
        for i in range(4):
            count = 0
            x,y = fx,fy # 반복을 할 때마다 x랑 y가 변한채로 진행이 되니 첫 시작을 다시 넣어줘야 한다.
            while True:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 > nx or nx == row or 0 > ny or ny == col or data[nx][ny] == 'D':
                    if data[x][y] == 'G':
                        return visited[fx][fy] + 1
                    if count > 0 and visited[fx][fy] + 1 < visited[x][y] : 
                        q.append((x,y))
                        visited[x][y] = visited[fx][fy] + 1
                    break
                x,y = nx,ny
                count += 1
    return -1
    
def solution(board):
    row = len(board)
    col = len(board[1])
    for i in range(row):
        for j in range(col):
            if board[i][j] == "R":
                return bfs(i,j,row,col,board)