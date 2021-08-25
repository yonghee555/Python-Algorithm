# 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [float('inf')] * (N + 1)
distance[X] = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

visited = [False] * (N + 1)
def bfs(start):
    q = deque()
    visited[start] = True
    q.append(start)
    while q:
        n = q.popleft()
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[n] + 1
                q.append(i)
bfs(X)

count = 0
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        count += 1
if count == 0:
    print(-1)