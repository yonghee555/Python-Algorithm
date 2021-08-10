# 효율적인 화폐 구성

currency = []
n, m = map(int, input().split())
for _ in range(n):
    c = int(input())
    currency.append(c)

d = [10001] * (m + 1)

d[0] = 0
for c in currency:
    for i in range(c, m + 1):
        if d[i - c] != 10001:
            d[i] = min(d[i], d[i - c] + 1)

print(-1 if d[m] == 10001 else d[m])