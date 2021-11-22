# 금광

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    dp = [0] * (n * m)
    for i in range(n):
        dp[0 + m * i] = data[0 + m * i]
    for i in range(m - 1):
        for j in range(n):
            now = j * m + i
            for x in range(-1 , 2):
                next = now + x * m + 1
                if 0 <= next < n * m:
                    dp[next] = max(dp[next], data[next] + dp[now])
    print(max(dp))
