# 전보

import heapq

INF = int(1e9)
n, m ,c = map(int, input().split())

graph = [[] for i in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distances = [INF] * (n + 1)

def dijkstra(start):
    q = []
    distances[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
time = 0
for i in range(1, n + 1):
    if distances[i] != INF:
        count += 1
        time = max(time, distances[i])

print(count - 1, time)