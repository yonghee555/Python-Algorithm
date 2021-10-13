# 인구 이동
# https://www.acmicpc.net/problem/16234
# PyPy3로 제출함

from collections import deque

N, L, R = map(int, input().split())
A = []
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
for _ in range(N):
    A.append(list(map(int, input().split())))

def bfs(i, j):
    global isMoved
    sum = 0 # 현재 연합의 총 인구수
    group = [] # 현재 나라와 연합을 맺은 국가들
    group.append((i, j))
    visited[i][j] = True
    q = deque() # BFS를 위한 큐
    q.append((i, j))
    while q:
        i, j = q.popleft()
        sum += A[i][j]
        for n in range(4):
            ni, nj = i + di[n], j + dj[n]
            if not 0 <= ni < N or not 0 <= nj < N or visited[ni][nj]:
                continue
            if L <= abs(A[i][j] - A[ni][nj]) <= R:
                if not isMoved: isMoved = True
                q.append((ni, nj))
                group.append((ni, nj))
                visited[ni][nj] = True
    sum //= len(group) # 연합의 총 인구 / 나라의 수
    for i, j in group:
        A[i][j] = sum

day = 0
while True:
    isMoved = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
    if isMoved: # 인구 이동이 있었을 경우 day += 1
        day += 1
    else: # 인구 이동이 없었을 경우 반복 종료
        break
print(day)