# 치킨 배달
# https://www.acmicpc.net/problem/15686

from itertools import combinations

N, M = map(int, input().split())
home = []
chicken = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            home.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))
answer = [] # 치킨 거리를 담는 배열
for comb in combinations(chicken, M):
    sum = 0 # 치킨 거리
    for h in home:
        dis = 100
        for c in comb:
            dis = min(dis, abs(c[0] - h[0]) + abs(c[1] - h[1]))
        sum += dis
    answer.append(sum)
print(min(answer))