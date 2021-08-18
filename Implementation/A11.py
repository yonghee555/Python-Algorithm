# 뱀
# https://www.acmicpc.net/problem/3190

from collections import deque

N = int(input())
K = int(input())

board = [[0] * (N + 1) for _ in range(N + 1)]
dir = {}
time = 0
head = [1, 1, 0] # 행, 열, 방향
body = deque()
drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]
for _ in range(K):
    row, col = map(int, input().split())
    board[row][col] = 1
L = int(input())
for _ in range(L):
    X, C = map(str, input().split())
    if C == 'L':
        dir[int(X)] = -1
    elif C == 'D':
        dir[int(X)] = 1
body.append((1,1))

while True:
    time += 1
    d = head[2]
    nrow, ncol = head[0] + drow[d], head[1] + dcol[d]
    if not 1 <= nrow <= N or not 1 <= ncol <= N or (nrow, ncol) in body:
        print(time)
        break
    head[0], head[1] = nrow, ncol
    if board[nrow][ncol] == 1:
        body.append((nrow, ncol))
        board[nrow][ncol] = 0
    else:
        body.append((nrow, ncol))
        body.popleft()
    if time in dir:
        head[2] = (head[2] + dir[time]) % 4