# 정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
array =list(map(int, input().split()))

count = bisect_right(array, x) - bisect_left(array, x)
print(-1 if count == 0 else count)