# 부품 찾기
# 계수 정렬을 이용한 풀이

N = int(input())
components = [0] * 1000001

for i in input().split():
    components[int(i)] = 1

M = int(input())
request = list(map(int, input().split()))

for i in request:
    print('yes' if components[i] else 'no', end=' ')
print()