# 큰 수의 법칙

# 방법 1
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
result = 0

while True:
    for _ in range(k):
        if m == 0: break
        result += numbers[-1]
        m -= 1
    if m == 0: break
    result += numbers[-2]
    m -= 1

print(result)

# 방법 2
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

count = m // (k + 1) * k + m % (k + 1)
result = numbers[-1] * count + numbers[-2] * (m - count)

print(result)