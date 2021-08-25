# 뱀
# https://www.acmicpc.net/problem/3190

from collections import deque

N = int(input())
K = int(input())

board = [[0] * (N + 1) for _ in range(N + 1)]
rotate = {}
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
        rotate[int(X)] = -1
    elif C == 'D':
        rotate[int(X)] = 1
body.append((1,1))

while True:
    time += 1
    d = head[2]
    nrow, ncol = head[0] + drow[d], head[1] + dcol[d]
    if not 1 <= nrow <= N or not 1 <= ncol <= N or (nrow, ncol) in body: # 벽 또는 자신의 몸을 만났을 때
        print(time)
        break
    head[0], head[1] = nrow, ncol
    if board[nrow][ncol] == 1: # 사과를 만났을 때
        body.append((nrow, ncol))
        board[nrow][ncol] = 0
    else: # 아무 것도 없는 칸으로 이동하였을 때
        body.append((nrow, ncol))
        body.popleft()
    if time in rotate: # time일 때 방향 변환이 있을 경우
        head[2] = (head[2] + rotate[time]) % 4