# 거스름돈

# 방법 1
n = 1260
count = 0

while n >= 500:
    n -= 500
    count += 1
while n >= 100:
    n -= 100
    count += 1
while n >= 50:
    n -= 50
    count += 1
while n >= 10:
    n -= 10
    count += 1

print(count)

# 방법 2
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)