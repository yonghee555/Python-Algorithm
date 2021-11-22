# 고정점 찾기

N = int(input())
array = list(map(int, input().split()))

start = 0
end = N - 1
answer = -1

while start <= end:
    mid = (start + end ) // 2
    if array[mid] == mid:
        answer = mid
        break
    if array[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1
print(answer)