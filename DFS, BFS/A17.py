# 경쟁적 전염
# https://www.acmicpc.net/problem/18405

from collections import deque
import sys

input = sys.stdin.readline

graph = []
virus = []
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, K = map(int, input().split())

for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(N):
        if row[j] != 0:
            virus.append((row[j], i, j)) # (바이러스 종류, 행, 열)

virus = deque(sorted(virus)) # 1번부터 순서대로 전염되기 때문에 오름차순으로 정렬
S, X, Y = map(int, input().split())

for _ in range(S):
    for _ in range(len(virus)):
        v, i, j = virus.popleft()
        for d in dir:
            nrow, ncol = i + d[0], j + d[1]
            if nrow < 0 or nrow >= N or ncol < 0 or ncol >= N or graph[nrow][ncol] != 0:
                continue
            graph[nrow][ncol] = v
            virus.append((v, nrow, ncol))
print(graph[X - 1][Y - 1])