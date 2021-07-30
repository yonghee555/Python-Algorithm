# 1이 될 때까지

# 방법 1
n, k = map(int, input().split())
result = 0

while n != 1:
    if n % k == 0:
        n /= k
    else:
        n -= 1
    result += 1

print(result)

# 방법 2
n, k = map(int, input().split())
result = 0

while True:
    # n % k == 0일 때까지 뺀다
    target = (n // k) * k
    result += n - target
    n = target

    if n < k:
        break
    result += 1
    n //= k

# 마지막 남은 수만큼 빼기
result += n - 1
print(result)