# 부품 찾기
# 이진 탐색을 이용한 풀이

N = int(input())
components = list(map(int, input().split()))
components.sort()
M = int(input())
request = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for i in request:
    print('yes' if binary_search(components, i, 0, N) else 'no', end=' ')
print()