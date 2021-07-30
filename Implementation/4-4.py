# 게임 개발

n, m = map(int, input().split())
a, b, d = map(int, input().split())

array = []
visited = [[0] * m for _ in range(n)]
count = 0

for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    d_temp = d
    d = (d - 1) % 4

    while d_temp != d:
        a_next, b_next = a + dx[d], b + dy[d]
        if array[a_next][b_next] == 1 or visited[a_next][b_next] == 1:
            d = (d - 1) % 4
        else:
            a, b = a_next, b_next
            count += 1
            visited[a][b] = 1
            break

    if d_temp == d:
        a_next = a - dx[d]
        b_next = b - dy[d]
        if array[a_next][b_next] == 1:
            break
        else:
            a, b = a_next, b_next

print(count)