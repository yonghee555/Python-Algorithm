# 떡볶이 떡 만들기

N, M = map(int, input().split())
h = list(map(int, input().split()))

start = 0
end = max(h)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in h:
        if x > mid:
            total += x - mid
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)